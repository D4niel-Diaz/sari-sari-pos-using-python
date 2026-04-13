from abc import ABC, abstractmethod


class IOutputWriter(ABC):

    @abstractmethod
    def write(self, data: str) -> None:
        pass