from fastapi import UploadFile, HTTPException
from fastapi.responses import JSONResponse
from answers_generator import QnA
from constants import FILE_DATA_TYPE_CONVERSIONS
from validators import QuestionFileValidate, DocumentFileValidate
from logging_config import logger

async def question_and_answers(questions_file: UploadFile, document_file: UploadFile):
    try:
        logger.info("Starting file data validations")
        questions = QuestionFileValidate(questions_file).parse()
        document = DocumentFileValidate(document_file).parse()
    except Exception as err:
        logger.exception(err.args[0])
        raise HTTPException(
            status_code=400,
            detail={"type": err.__class__.__name__, "message": err.args[0]},
        )
    else:
        try:
            logger.info("Starting answer generation process....")
            questions_answers = QnA(
                questions,
                document,
                FILE_DATA_TYPE_CONVERSIONS[document_file.content_type],
            ).get_answers()
            logger.info("Answer generation process is complete")
            return JSONResponse(questions_answers, status_code=200)
        except Exception as err:
            raise HTTPException(
                status_code=400,
                details={
                    "type": "FailedToGenerateAnswers",
                    "message": "Failed to generate answers",
                },
            )
