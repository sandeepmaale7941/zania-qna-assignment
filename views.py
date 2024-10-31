from fastapi import UploadFile, HTTPException
from fastapi.responses import JSONResponse
from answers_generator import QnA
from constants import FILE_DATA_TYPE_CONVERSIONS
from validators import QuestionFileValidate, DocumentFileValidate


async def question_and_answers(questions_file: UploadFile, document_file: UploadFile):
    try:
        questions = QuestionFileValidate(questions_file).parse()
        document = DocumentFileValidate(document_file).parse()
    except Exception as err:
        raise HTTPException(
            status_code=400,
            detail={"type": err.__class__.__name__, "message": err.args[0]},
        )
    else:
        try:
            questions_answers = QnA(
                questions,
                document,
                FILE_DATA_TYPE_CONVERSIONS[document_file.content_type],
            ).get_answers()
            return JSONResponse(questions_answers, status_code=200)
        except Exception as err:
            raise HTTPException(
                status_code=400,
                details={
                    "type": "FailedToGenerateAnswers",
                    "message": "Failed to generate answers",
                },
            )
