import json
from app.core.inventory import InventorySystem
from app.core.transaction import SalesTransaction
from app.interfaces.i_input_reader import IInputReader
from app.interfaces.i_output_writer import IOutputWriter
from app.reports.report_generator import ReportGenerator


class POSApp:

    def __init__(self, reader: IInputReader, writer: IOutputWriter,
                 inventory: InventorySystem, report_generator: ReportGenerator):
        self._reader = reader
        self._writer = writer
        self._inventory = inventory
        self._report_generator = report_generator
        self._transactions = []
        self._transaction_counter = 1

    def _load_products(self, filepath: str) -> None:
        with open(filepath, "r") as f:
            data = json.load(f)
        self._inventory._load_from_list(data)

    def _save_products(self, filepath: str) -> None:
        with open(filepath, "w") as f:
            json.dump(self._inventory.to_list(), f, indent=4)

    def _load_transactions(self, filepath: str) -> None:
        with open(filepath, "r") as f:
            self._transactions = json.load(f)

    def _save_transactions(self, filepath: str) -> None:
        with open(filepath, "w") as f:
            json.dump(self._transactions, f, indent=4)

    def process_sale(self) -> None:
        data = self._reader.read()
        product = self._inventory.get_product(data["product_id"])
        transaction_id = f"TXN{self._transaction_counter:04d}"
        transaction = SalesTransaction(transaction_id)
        transaction.add_item(product, data["quantity"])
        self._transactions.append(transaction.to_dict())
        self._transaction_counter += 1
        self._writer.write(transaction.get_summary())

    def view_inventory(self) -> None:
        products = self._inventory.view_products()
        for product in products:
            self._writer.write(product)

    def generate_report(self, filepath: str) -> None:
        report = self._report_generator.generate(self._transactions)
        self._writer.write(report)
        self._report_generator.save(self._transactions, filepath)
        self._writer.write(f"\nReport saved to: {filepath}")