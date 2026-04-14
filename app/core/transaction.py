from datetime import datetime
from app.core.product import Product


class SalesTransaction:

    def __init__(self, transaction_id: str):
        self._transaction_id = transaction_id
        self._items = []
        self._total = 0.0
        self._date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def transaction_id(self) -> str:
        return self._transaction_id

    @property
    def items(self) -> list:
        return self._items

    @property
    def total(self) -> float:
        return self._total

    @property
    def date(self) -> str:
        return self._date

    def add_item(self, product: Product, quantity: int) -> None:
        if not product._is_available(quantity):
            raise ValueError(f"Insufficient stock for '{product.name}'.")
        product.update_stock(quantity)
        subtotal = product.price * quantity
        self._items.append({
            "product_id": product.product_id,
            "name": product.name,
            "quantity": quantity,
            "subtotal": subtotal
        })
        self._total += subtotal

    def _calculate_total(self) -> float:
        return sum(item["subtotal"] for item in self._items)

    def to_dict(self) -> dict:
        return {
            "transaction_id": self._transaction_id,
            "date": self._date,
            "items": self._items,
            "total": self._total
        }

    def get_summary(self) -> str:
        lines = [f"Transaction ID : {self._transaction_id}",
                 f"Date           : {self._date}"]
        for item in self._items:
            lines.append(f"  {item['name']} x{item['quantity']} = ₱{item['subtotal']:.2f}")
        lines.append(f"Total          : ₱{self._total:.2f}")
        return "\n".join(lines)