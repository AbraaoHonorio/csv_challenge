from abc import abstractmethod
from typing import Dict, TypeVar

T = TypeVar("T")


class ReadDataInterface:
    def __init__(self):
        pass

    @abstractmethod
    def load_data_by_type(self, type_data: T) -> Dict[int, T]:
        raise NotImplementedError()
