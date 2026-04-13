from abc import ABC, abstractmethod


class IInputReader(ABC):

    @abstractmethod
    def read(self) -> dict:
        pass