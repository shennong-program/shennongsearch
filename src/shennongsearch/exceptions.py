class ShennongSearchError(Exception):
    def __init__(self, message: str, status_code: int | None = None, user_message: str | None = None):
        super().__init__(message)
        self.status_code = status_code
        self.user_message = user_message

    def __str__(self) -> str:
        base = super().__str__()
        if self.status_code is None:
            return base
        if self.user_message:
            return f"{base} (status={self.status_code}, user_message={self.user_message})"
        return f"{base} (status={self.status_code})"
