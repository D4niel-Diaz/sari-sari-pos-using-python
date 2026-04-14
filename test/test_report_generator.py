from app.reports.report_generator import ReportGenerator
from app.interfaces.i_report_formatter import IReportFormatter


class FakeFormatter(IReportFormatter):
    def format(self, transactions: list) -> str:
        return f"FAKE REPORT: {len(transactions)} transaction(s)"


def test_generate_returns_formatted_string():
    formatter = FakeFormatter()
    generator = ReportGenerator(formatter)
    transactions = [{"transaction_id": "TXN0001", "items": [], "total": 0.0}]
    result = generator.generate(transactions)
    assert result == "FAKE REPORT: 1 transaction(s)"


def test_generate_with_empty_transactions():
    formatter = FakeFormatter()
    generator = ReportGenerator(formatter)
    result = generator.generate([])
    assert result == "FAKE REPORT: 0 transaction(s)"


def test_generate_with_multiple_transactions():
    formatter = FakeFormatter()
    generator = ReportGenerator(formatter)
    transactions = [
        {"transaction_id": "TXN0001", "items": [], "total": 0.0},
        {"transaction_id": "TXN0002", "items": [], "total": 0.0}
    ]
    result = generator.generate(transactions)
    assert result == "FAKE REPORT: 2 transaction(s)"