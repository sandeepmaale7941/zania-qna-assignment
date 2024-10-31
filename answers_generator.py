from langchain.chains import RetrievalQA

from llms import LLMFinder
from content_splitter import RecursiveSplitter
from vectordb import VectorDB

from logging_config import logger
from embeddings import get_embedding

class QnA:
    def __init__(self, questions, file_content, data_type):
        self.questions = questions
        self.file_content = file_content
        self.data_type = data_type

    def get_answers(self):
        try:
            splits = RecursiveSplitter.split(self.file_content, self.data_type)
            logger.info("Data Splitting complete!!!")
            embedding = get_embedding()
            logger.info("Starting vector db generation...")
            vectordb = VectorDB(splits, embedding).get_vectordb()
            logger.info("Vectordb generation complete")
            llm = LLMFinder.get_llm()

            qa_chain = RetrievalQA.from_chain_type(
                llm, retriever=vectordb.as_retriever(search_kwargs={"k": 2})
            )
            logger.info("Starting answer generation....")
            question_answers_map = {}
            for question in self.questions:
                result = qa_chain.invoke({"query": question})
                question_answers_map[question] = result["result"]
            logger.info("Answer generation complete")
            return question_answers_map
        except Exception as err:
            logger.exception(f"Error: {err.args[0]}, ErrorType: {err.__class__.__name__}")
            raise err
