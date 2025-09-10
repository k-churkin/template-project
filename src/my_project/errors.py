from http import HTTPStatus


class BaseError(Exception):
    """Base class for all application errors."""

    message: str = "Unknown error"
    def __init__(self, *, message: str | None = None, **ctx):
        if message:
            self.message = message
        super().__init__(message)
        self.ctx = ctx



class ApplicationError(BaseError):
    HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, *, message: str | None = None, status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR,  **ctx):
        super().__init__(message=message, ctx=ctx)
        self.status_code = status_code

