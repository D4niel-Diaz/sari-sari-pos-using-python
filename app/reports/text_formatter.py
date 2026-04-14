from app.interfaces.i_report_formatter import IReportFormatter


class TextFormatter(IReportFormatter):

    def format(self, transactions: list) -> str:
        lines = ["=" * 40]
        lines.append("       SARI-SARI POS SALES REPORT")
        lines.append("=" * 40)
        total_revenue = 0.0

        for t in transactions:
            lines.append(f"Transaction ID : {t['transaction_id']}")
            lines.append(f"Date           : {t['date']}")
            for item in t["items"]:
                lines.append(f"  {item['name']} x{item['quantity']} = ₱{item['subtotal']:.2f}")
            lines.append(f"Total          : ₱{t['total']:.2f}")
            lines.append("-" * 40)
            total_revenue += t["total"]

        lines.append(f"TOTAL REVENUE  : ₱{total_revenue:.2f}")
        lines.append("=" * 40)
        return "\n".join(lines)