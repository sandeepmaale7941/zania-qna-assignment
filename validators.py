import json
import PyPDF2
from abc import ABC, abstractmethod
from fastapi import UploadFile
from io import BytesIO
from typing import List


from constants import FileTypes

class BaseParser(ABC):
    def __init__(self, file: UploadFile):
        self.file = file

    @abstractmethod
    def extract_data(self):
        raise NotImplementedError()

class JSONFileParser(BaseParser):
    def validate_type(self):
        return self.file.content_type == FileTypes.JSON

    def extract_data(self):
        try:
            return json.load(self.file.file)
        except Exception as err:
            raise InvalidJSONData() # TODO: Write proper error message

class PDFFileParser(BaseParser):
    
    def validate_type(self):
        return self.file.content_type == FileTypes.PDF
    
    def extract_data(self):
        # TODO: Add try catch block 
        pdf_reader = PyPDF2.PdfReader(BytesIO(self.file.file.read()))
        content = "\n".join([page.extract_text() for page in pdf_reader.pages])
        return content

class BaseFileValidator:

    FILE_TYPE_PARSERS = {
        FileTypes.JSON: JSONFileParser,
        FileTypes.PDF: PDFFileParser
    }

    def __init__(self, file: UploadFile):
        self.file = file
    
    def validate_file_types(self, valid_types: List[str]) -> bool:
        return self.file.content_type in valid_types
    
    def extract_data(self):
        try:
            return BaseFileValidator.FILE_TYPE_PARSERS[self.file.content_type](self.file).extract_data()
        except Exception as err:
            # TODO: Return Proper error message
            pass
    
    def validate_and_extract_data(self, valid_file_types: List[str]):
        self.validate_file_types(valid_file_types)
        return self.extract_data()
    
    @abstractmethod
    def parse():
        raise NotImplementedError

class QuestionFileValidate(BaseFileValidator):
    VALID_FILE_TYPES = [FileTypes.JSON]

    def parse(self):
        return self.validate_and_extract_data(QuestionFileValidate.VALID_FILE_TYPES)

class DocumentFileValidate(BaseFileValidator):
    VALID_FILE_TYPES = [FileTypes.JSON, FileTypes.PDF]

    def parse(self):
        return self.validate_and_extract_data(QuestionFileValidate.VALID_FILE_TYPES)
