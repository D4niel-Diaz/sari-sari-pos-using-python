import pytest
from app.core.product import Product
from app.core.transaction import SalesTransaction


def test_add_item_calculates_subtotal():
    product = Product("P001", "Coca-Cola", 22.00, 50)
    transaction = SalesTransaction("TXN0001")
    transaction.add_item(product, 3)
    assert transaction.items[0]["subtotal"] == 66.00


def test_add_item_updates_total():
    product = Product("P002", "Lucky Me", 15.00, 100)
    transaction = SalesTransaction("TXN0002")
    transaction.add_item(product, 5)
    assert transaction.total == 75.00


def test_add_item_raises_error_when_insufficient_stock():
    product = Product("P003", "Bear Brand", 85.00, 2)
    transaction = SalesTransaction("TXN0003")
    with pytest.raises(ValueError):
        transaction.add_item(product, 10)