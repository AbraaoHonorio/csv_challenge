from abc import ABC, abstractmethod


class ProcessorBase(ABC):
    @abstractmethod
    def process(self, data) -> None:
        pass
