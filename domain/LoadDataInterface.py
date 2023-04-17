from abc import abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class LoadDataInterface(Generic[T]):
    def __init__(self, ):
        pass

    @abstractmethod
    def load_data(self, type:T) -> T:
        raise NotImplementedError()
