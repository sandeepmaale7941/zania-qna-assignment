import os
import importlib
from abc import abstractmethod
from langchain_community.chat_models import ChatOpenAI as COAI
from langchain_ollama import ChatOllama as ChOll


class BaseLLM:
    @abstractmethod
    def llm():
        raise NotImplementedError


class ChatOllama(BaseLLM):
    def llm():
        model_name = os.environ["MODEL_NAME"]
        return ChOll(
            model="llama3.2",
        )


class ChatOpenAI(BaseLLM):
    def llm():
        model_name = os.environ["MODEL_NAME"]
        return COAI(model_name=model_name, temperature=0)


class LLMFinder:
    def get_llm():
        module = importlib.import_module(__name__)
        chat_model = os.environ["CHATMODEL"]
        return getattr(module, chat_model).llm()
