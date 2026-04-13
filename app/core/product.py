class Product:

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def stock(self) -> int:
        return self._stock

    def update_stock(self, quantity: int) -> None:
        if quantity > self._stock:
            raise ValueError(f"Not enough stock for '{self._name}'.")
        self._stock -= quantity

    def _is_available(self, quantity: int) -> bool:
        return self._stock >= quantity

    def to_dict(self) -> dict:
        return {
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock
        }

    def __str__(self) -> str:
        return f"[{self._product_id}] {self._name} - ₱{self._price:.2f} (Stock: {self._stock})"