from fastapi import UploadFile, HTTPException
from fastapi.responses import JSONResponse
from langchain_community.llms import OpenAI
from answers_generator import QnA
from constants import DataTypes, FILE_DATA_TYPE_CONVERSIONS
from validators import QuestionFileValidate, DocumentFileValidate

async def question_and_answers(questions_file: UploadFile, document_file: UploadFile):
    try:
        questions = QuestionFileValidate(questions_file).parse()
        document = DocumentFileValidate(document_file).parse()
        questions_answers = QnA(questions, document, FILE_DATA_TYPE_CONVERSIONS[document_file.content_type]).get_answers()
        return JSONResponse(questions_answers, status_code=200)
    except Exception as err:
        pass
