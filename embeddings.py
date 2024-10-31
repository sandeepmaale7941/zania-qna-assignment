import os
import importlib
from abc import abstractmethod

from langchain_community.embeddings.openai import OpenAIEmbeddings as OAIE
from langchain_ollama import OllamaEmbeddings as OlE


class BaseEmbedding:
    @abstractmethod
    def embedding():
        raise NotImplementedError


class OllamaEmbeddings(BaseEmbedding):
    def embedding():
        return OlE(model=os.environ["EMBEDDING_MODEL_NAME"])


class OpenAIEmbeddings(BaseEmbedding):
    def embedding():
        return OAIE()


def get_embedding():
    module = importlib.import_module(__name__)
    return getattr(module, os.environ["EMBEDDING"]).embedding()
