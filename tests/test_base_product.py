import pytest

from src.base_product import BaseProduct
from src.lawn_grass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone


def test_base_product_is_abstract() -> None:
    """Проверяет, что BaseProduct является абстрактным классом."""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Description", 100.0, 5)


def test_product_inherits_from_base_product() -> None:
    """Проверяет наследование Product от BaseProduct."""
    product = Product("Test Product", "Description", 100.0, 5)
    assert isinstance(product, BaseProduct)


def test_product_get_total_value() -> None:
    """Проверяет метод get_total_value."""
    product = Product("Test Product", "Description", 100.0, 5)
    assert product.get_total_value() == 500.0


def test_product_is_available() -> None:
    """Проверяет метод is_available."""
    product = Product("Test Product", "Description", 100.0, 5)
    assert product.is_available() is True

    product.quantity = 0
    assert product.is_available() is False


def test_product_get_info() -> None:
    """Проверяет метод get_info."""
    product = Product("Test Product", "Description", 100.0, 5)
    info = product.get_info()

    assert info["name"] == "Test Product"
    assert info["description"] == "Description"
    assert info["price"] == 100.0
    assert info["quantity"] == 5
    assert info["total_value"] == 500.0
    assert info["available"] is True


def test_smartphone_inheritance() -> None:
    """Проверяет наследование Smartphone."""
    smartphone = Smartphone(
        "iPhone", "Description", 1000.0, 3, 95.5, "15", 256, "Black"
    )
    assert isinstance(smartphone, BaseProduct)
    assert isinstance(smartphone, Product)


def test_lawn_grass_inheritance() -> None:
    """Проверяет наследование LawnGrass."""
    grass = LawnGrass("Grass", "Description", 100.0, 10, "Russia", "7 days", "Green")
    assert isinstance(grass, BaseProduct)
    assert isinstance(grass, Product)


def test_smartphone_get_specifications() -> None:
    """Проверяет метод get_specifications у Smartphone."""
    smartphone = Smartphone(
        "iPhone", "Description", 1000.0, 3, 95.5, "15", 256, "Black"
    )
    specs = smartphone.get_specifications()

    assert specs["efficiency"] == 95.5
    assert specs["model"] == "15"
    assert specs["memory"] == 256
    assert specs["color"] == "Black"


def test_lawn_grass_get_growing_info() -> None:
    """Проверяет метод get_growing_info у LawnGrass."""
    grass = LawnGrass("Grass", "Description", 100.0, 10, "Russia", "7 days", "Green")
    info = grass.get_growing_info()

    assert info["country"] == "Russia"
    assert info["germination_period"] == "7 days"
    assert info["color"] == "Green"
