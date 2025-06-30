class DatabaseConnectionException(Exception):
    def __init__(self, message="Database connection error"):
        super().__init__(message)
