from app.interfaces.i_input_reader import IInputReader


class ConsoleReader(IInputReader):

    def read(self) -> dict:
        print("\n--- New Sale ---")
        product_id = input("Enter Product ID: ").strip()
        quantity = int(input("Enter Quantity: ").strip())
        return {
            "product_id": product_id,
            "quantity": quantity
        }