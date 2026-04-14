from app.interfaces.i_report_formatter import IReportFormatter


class ReportGenerator:

    def __init__(self, formatter: IReportFormatter):
        self._formatter = formatter

    def generate(self, transactions: list) -> str:
        return self._formatter.format(transactions)

    def save(self, transactions: list, filepath: str) -> None:
        report = self._formatter.format(transactions)
        with open(filepath, "w") as f:
            f.write(report)