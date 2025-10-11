import pytest

from src.smartphone_product import Smartphone



def test_smartphone_product_init_field():
    s = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    assert s.name == "Samsung Galaxy S23 Ultra"
    assert s.price == 180000.0
    assert s.quantity == 5
    assert s.efficiency == 95.5
    assert s.model == "S23 Ultra"
    assert s.memory == 256
    assert s.color == "Серый"