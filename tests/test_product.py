from src.product import Product


def test_product_init_fields() -> None:
    p = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert p.name == "Samsung Galaxy S23 Ultra"
    assert p.description == "256GB, Серый цвет, 200MP камера"
    assert p.price == 180000.0
    assert p.quantity == 5
