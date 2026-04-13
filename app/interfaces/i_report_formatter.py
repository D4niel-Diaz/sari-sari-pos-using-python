from abc import ABC, abstractmethod


class IReportFormatter(ABC):

    @abstractmethod
    def format(self, transactions: list) -> str:
        pass