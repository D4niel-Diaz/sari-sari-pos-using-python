import pytest
from app.core.product import Product


def test_product_initial_stock():
    product = Product("P001", "Coca-Cola", 22.00, 50)
    assert product.stock == 50


def test_update_stock_reduces_correctly():
    product = Product("P001", "Coca-Cola", 22.00, 50)
    product.update_stock(10)
    assert product.stock == 40


def test_update_stock_raises_error_when_insufficient():
    product = Product("P001", "Coca-Cola", 22.00, 5)
    with pytest.raises(ValueError):
        product.update_stock(10)