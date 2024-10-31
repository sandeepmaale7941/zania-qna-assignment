class FileTypes:
    JSON = "application/json"
    PDF = "application/pdf"


QUESTIONS_FILE_TYPE = FileTypes.JSON

DOCUMENT_FILE_TYPE = [FileTypes.JSON, FileTypes.PDF]


class DataTypes:
    JSON = "json"
    TEXT = "text"


FILE_DATA_TYPE_CONVERSIONS = {
    FileTypes.JSON: DataTypes.JSON,
    FileTypes.PDF: DataTypes.TEXT,
}
