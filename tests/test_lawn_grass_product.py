import pytest

from src.lawn_grass_product import LawnGrass


def test_lawn_grass_product_init_field():
    lg = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )
    assert lg.name == "Газонная трава"
    assert lg.description == "Элитная трава для газона"
    assert lg.price == 500.0
    assert lg.quantity == 20
    assert lg.country == "Россия"
    assert lg.germination_period == "7 дней"
    assert lg.color == "Зеленый"