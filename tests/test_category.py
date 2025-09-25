from src.category import Category
from src.product import Product


def test_category_init_and_counters_single_category() -> None:
    p1 = Product("A", "desc A", 10.0, 1)
    p2 = Product("B", "desc B", 20.0, 2)
    cat = Category("Смартфоны", "Описание", [p1, p2])

    assert cat.name == "Смартфоны"
    assert cat.description == "Описание"
    assert len(cat.products) == 2

    # атрибуты класса увеличены корректно
    assert Category.category_count == 1
    assert Category.product_count == 2

    # доступ к атрибутам класса через экземпляр
    assert cat.category_count == Category.category_count
    assert cat.product_count == Category.product_count


def test_category_counters_accumulate_across_instances() -> None:
    p1 = Product("A", "d", 10.0, 1)
    p2 = Product("B", "d", 20.0, 2)
    p3 = Product("C", "d", 30.0, 3)

    cat1 = Category("Смартфоны", "D1", [p1, p2])
    cat2 = Category("Телевизоры", "D2", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3

    # экземпляры отражают те же значения атрибутов класса
    assert cat1.category_count == 2
    assert cat2.category_count == 2
    assert cat1.product_count == 3
    assert cat2.product_count == 3


def test_product_init_fields() -> None:
    p = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert p.name == "Samsung Galaxy S23 Ultra"
    assert p.description == "256GB, Серый цвет, 200MP камера"
    assert p.price == 180000.0
    assert p.quantity == 5
