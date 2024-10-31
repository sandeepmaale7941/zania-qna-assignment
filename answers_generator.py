from langchain.chains import RetrievalQA

from embeddings import get_embedding
from llms import LLMFinder
from content_splitter import RecursiveSplitter
from vectordb import VectorDB


class QnA:
    def __init__(self, questions, file_content, data_type):
        self.questions = questions
        self.file_content = file_content
        self.data_type = data_type

    def get_answers(self):

        splits = RecursiveSplitter.split(self.file_content, self.data_type)
        embedding = get_embedding()
        vectordb = VectorDB(splits, embedding).get_vectordb()
        llm = LLMFinder.get_llm()

        qa_chain = RetrievalQA.from_chain_type(
            llm, retriever=vectordb.as_retriever(search_kwargs={"k": 2})
        )

        question_answers_map = {}
        for question in self.questions:
            result = qa_chain.invoke({"query": question})
            question_answers_map[question] = result["result"]
        return question_answers_map
