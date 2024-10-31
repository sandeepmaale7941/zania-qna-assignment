from fastapi import APIRouter
from views import question_and_answers

q_n_a_router = APIRouter()
q_n_a_router.post("/qna")(question_and_answers)
