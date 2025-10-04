import pytest

from src.product import Product


def test_product_init_fields() -> None:
    """Проверяет корректность инициализации полей товара."""
    p = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert p.name == "Samsung Galaxy S23 Ultra"
    assert p.description == "256GB, Серый цвет, 200MP камера"
    assert p.price == 180000.0
    assert p.quantity == 5


def test_product_price_getter() -> None:
    """Проверяет работу геттера цены."""
    p = Product("Test", "Test desc", 100.0, 1)
    assert p.price == 100.0


def test_product_price_setter_positive() -> None:
    """Проверяет работу сеттера цены с положительным значением."""
    p = Product("Test", "Test desc", 100.0, 1)
    p.price = 150.0
    assert p.price == 150.0


def test_product_price_setter_negative(capsys):
    """Проверяет работу сеттера цены с отрицательным значением."""
    p = Product("Test", "Test desc", 100.0, 1)
    p.price = -50.0
    assert p.price == 100.0  # цена не изменилась
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_price_setter_zero(capsys):
    """Проверяет работу сеттера цены с нулевым значением."""
    p = Product("Test", "Test desc", 100.0, 1)
    p.price = 0.0
    assert p.price == 100.0  # цена не изменилась
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_str() -> None:
    """Проверяет строковое представление продукта."""
    p = Product("Test Product", "Test Description", 150.0, 3)
    expected = "Test Product, 150.0 руб. Остаток: 3 шт."
    assert str(p) == expected


def test_product_add() -> None:
    """Проверяет магический метод сложения продуктов."""
    p1 = Product("Product 1", "Desc 1", 100.0, 5)
    p2 = Product("Product 2", "Desc 2", 200.0, 3)

    result = p1 + p2
    expected = 100.0 * 5 + 200.0 * 3  # 500 + 600 = 1100
    assert result == expected


def test_product_add_type_error() -> None:
    """Проверяет ошибку типа при сложении с не-Product объектом."""
    p = Product("Test", "Desc", 100.0, 1)

    with pytest.raises(
        TypeError, match="Можно складывать только объекты класса Product"
    ):
        p + "not a product"


def test_product_new_product_classmethod() -> None:
    """Проверяет работу класс-метода new_product."""
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 200.0,
        "quantity": 3,
    }
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 200.0
    assert product.quantity == 3


def test_product_new_product_with_duplicate_check() -> None:
    """Проверяет работу класс-метода с проверкой дубликатов."""
    existing_products = [Product("Existing Product", "Desc", 100.0, 5)]

    product_data = {
        "name": "existing product",  # то же имя, но в нижнем регистре
        "description": "New Desc",
        "price": 150.0,  # более высокая цена
        "quantity": 3,
    }

    result = Product.new_product_with_duplicate_check(product_data, existing_products)

    # Должен вернуть существующий продукт
    assert result is existing_products[0]
    assert result.quantity == 8  # 5 + 3
    assert result.price == 150.0  # выбрана более высокая цена


def test_product_new_product_with_duplicate_check_no_duplicate() -> None:
    """Проверяет создание нового продукта при отсутствии дубликатов."""
    existing_products = [Product("Existing Product", "Desc", 100.0, 5)]

    product_data = {
        "name": "New Product",
        "description": "New Desc",
        "price": 150.0,
        "quantity": 3,
    }

    result = Product.new_product_with_duplicate_check(product_data, existing_products)

    # Должен создать новый продукт
    assert result is not existing_products[0]
    assert result.name == "New Product"
    assert result.price == 150.0
    assert result.quantity == 3
