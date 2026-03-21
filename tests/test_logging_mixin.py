from src.lawn_grass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone


def test_product_logging(capsys):
    """Проверяет логирование создания Product."""
    product = Product("Test Product", "Description", 100.0, 5)
    captured = capsys.readouterr()

    assert "Product('Test Product', 'Description', 100.0, 5)" in captured.out
    # Дополнительная проверка, что объект создался корректно
    assert product.name == "Test Product"
    assert product.price == 100.0


def test_smartphone_logging(capsys):
    """Проверяет логирование создания Smartphone."""
    smartphone = Smartphone(
        "iPhone", "Description", 1000.0, 3, 95.5, "15", 256, "Black"
    )
    captured = capsys.readouterr()

    assert (
        "Smartphone('iPhone', 'Description', 1000.0, 3, 95.5, '15', 256, 'Black')"
        in captured.out
    )
    # Дополнительная проверка, что объект создался корректно
    assert smartphone.name == "iPhone"
    assert smartphone.efficiency == 95.5


def test_lawn_grass_logging(capsys):
    """Проверяет логирование создания LawnGrass."""
    grass = LawnGrass("Grass", "Description", 100.0, 10, "Russia", "7 days", "Green")
    captured = capsys.readouterr()

    assert (
        "LawnGrass('Grass', 'Description', 100.0, 10, 'Russia', '7 days', 'Green')"
        in captured.out
    )
    # Дополнительная проверка, что объект создался корректно
    assert grass.name == "Grass"
    assert grass.country == "Russia"


def test_product_repr() -> None:
    """Проверяет метод __repr__ у Product."""
    product = Product("Test Product", "Description", 100.0, 5)
    repr_str = repr(product)

    assert repr_str == "Product('Test Product', 'Description', 100.0, 5)"


def test_smartphone_repr() -> None:
    """Проверяет метод __repr__ у Smartphone."""
    smartphone = Smartphone(
        "iPhone", "Description", 1000.0, 3, 95.5, "15", 256, "Black"
    )
    repr_str = repr(smartphone)

    assert (
        repr_str
        == "Smartphone('iPhone', 'Description', 1000.0, 3, 95.5, '15', 256, 'Black')"
    )


def test_lawn_grass_repr():
    """Проверяет метод __repr__ у LawnGrass."""
    grass = LawnGrass("Grass", "Description", 100.0, 10, "Russia", "7 days", "Green")
    repr_str = repr(grass)

    assert (
        repr_str
        == "LawnGrass('Grass', 'Description', 100.0, 10, 'Russia', '7 days', 'Green')"
    )
