import json
import os
from app.core.inventory import InventorySystem
from app.io.console_reader import ConsoleReader
from app.io.screen_writer import ScreenWriter
from app.reports.report_generator import ReportGenerator
from app.reports.text_formatter import TextFormatter
from app.pos_app import POSApp

PRODUCTS_FILE = "data/products.json"
TRANSACTIONS_FILE = "data/transactions.json"
REPORTS_FILE = "reports/sales_report.txt"


def _initialize_data_files():
    if os.path.getsize(PRODUCTS_FILE) == 0:
        with open(PRODUCTS_FILE, "w") as f:
            json.dump([], f)
    if os.path.getsize(TRANSACTIONS_FILE) == 0:
        with open(TRANSACTIONS_FILE, "w") as f:
            json.dump([], f)


def main():
    _initialize_data_files()

    inventory = InventorySystem()
    reader = ConsoleReader()
    writer = ScreenWriter()
    formatter = TextFormatter()
    report_generator = ReportGenerator(formatter)

    app = POSApp(reader, writer, inventory, report_generator)

    app._load_products(PRODUCTS_FILE)
    app._load_transactions(TRANSACTIONS_FILE)

    while True:
        print("\n====== SARI-SARI POS ======")
        print("[1] View Inventory")
        print("[2] Process Sale")
        print("[3] Generate Report")
        print("[4] Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            app.view_inventory()
        elif choice == "2":
            try:
                app.process_sale()
                app._save_products(PRODUCTS_FILE)
                app._save_transactions(TRANSACTIONS_FILE)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            app.generate_report(REPORTS_FILE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()