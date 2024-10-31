from langchain_community.vectorstores import Chroma


class VectorDB:
    def __init__(self, splits: str, embedding):
        self.splits = splits
        self.embedding = embedding

    def get_vectordb(self):
        vectordb = Chroma.from_texts(texts=self.splits, embedding=self.embedding)
        return vectordb
