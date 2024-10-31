class InvalidFileType(Exception):
    def __init__(self, message="Invalid File Type"):
        self.message = message
        super().__init__(message)


class InvalidData(Exception):
    def __init__(self, message="File contains invalid data"):
        self.message = message
        super().__init__(message)
