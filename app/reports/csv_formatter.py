from app.interfaces.i_report_formatter import IReportFormatter


class CSVFormatter(IReportFormatter):

    def format(self, transactions: list) -> str:
        lines = ["transaction_id,date,product_name,quantity,subtotal,total"]

        for t in transactions:
            for item in t["items"]:
                lines.append(
                    f"{t['transaction_id']},"
                    f"{t['date']},"
                    f"{item['name']},"
                    f"{item['quantity']},"
                    f"{item['subtotal']:.2f},"
                    f"{t['total']:.2f}"
                )

        return "\n".join(lines)