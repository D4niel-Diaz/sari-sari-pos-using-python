from app.core.product import Product


class InventorySystem:

    def __init__(self):
        self._products = {}

    @property
    def products(self) -> dict:
        return self._products

    def add_product(self, product: Product) -> None:
        if product.product_id in self._products:
            raise ValueError(f"Product ID '{product.product_id}' already exists.")
        self._products[product.product_id] = product

    def get_product(self, product_id: str) -> Product:
        if product_id not in self._products:
            raise ValueError(f"Product ID '{product_id}' not found.")
        return self._products[product_id]

    def update_product(self, product_id: str, price: float = None, stock: int = None) -> None:
        product = self.get_product(product_id)
        if price is not None:
            product._price = price
        if stock is not None:
            product._stock = stock

    def view_products(self) -> list:
        return [str(product) for product in self._products.values()]

    def _load_from_list(self, data: list) -> None:
        for item in data:
            product = Product(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"]
            )
            self._products[product.product_id] = product

    def to_list(self) -> list:
        return [p.to_dict() for p in self._products.values()]