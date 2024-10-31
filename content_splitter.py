from abc import abstractmethod

from langchain_text_splitters import RecursiveJsonSplitter as RJS
from langchain_text_splitters import RecursiveCharacterTextSplitter as RCTS

from constants import DataTypes


class BaseRecursiveSpllitter:
    @abstractmethod
    def splits(self):
        raise NotImplementedError


class RecursiveJsonSplitter(BaseRecursiveSpllitter):
    def splits(data):
        splitter = RJS()
        json_chunks = splitter.split_text(json_data=data, convert_lists=True)
        return json_chunks


class RecursiveCharacterTextSplitter(BaseRecursiveSpllitter):
    def splits(data):
        splitter = RCTS()
        texts = splitter.split_text(data)
        return texts


class RecursiveSplitter:
    DATA_TYPE_CLASS_MAP = {
        DataTypes.TEXT: RecursiveCharacterTextSplitter,
        DataTypes.JSON: RecursiveJsonSplitter,
    }

    def split(data, data_type):
        return RecursiveSplitter.DATA_TYPE_CLASS_MAP[data_type].splits(data)
