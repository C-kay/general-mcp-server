class BearerAuthASGIMiddleware:
    def __init__(self, app, token: str):
        self.app = app
        self.token = token

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            path = scope.get("path", "")
            # protect Streamable HTTP endpoints (/mcp and children)
            if path == "/mcp" or path.startswith("/mcp/"):
                # headers are a list of (name, value) in bytes
                hdrs = {k.decode().lower(): v.decode() for k, v in scope.get("headers", [])}
                auth = hdrs.get("authorization", "")
                if not auth.lower().startswith("bearer "):
                    await _plain(send, 401, "Unauthorized", [("www-authenticate", "Bearer")])
                    return
                token = auth.split(" ", 1)[1].strip()
                if token != self.token:
                    await _plain(send, 403, "Forbidden")
                    return
        # pass through
        await self.app(scope, receive, send)

async def _plain(send, status: int, text: str, extra_headers=None):
    headers = [(b"content-type", b"text/plain; charset=utf-8")]
    if extra_headers:
        headers += [(k.encode(), v.encode()) for k, v in extra_headers]
    await send({"type": "http.response.start", "status": status, "headers": headers})
    await send({"type": "http.response.body", "body": text.encode(), "more_body": False})
