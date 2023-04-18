class CsvNotFound(Exception):
    def __init__(self, message: str, e: Exception):
        super().__init__(message, e)
