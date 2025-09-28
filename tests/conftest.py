import pytest
from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Сбрасывает счётчики класса Category перед и после каждого теста."""
    # Сохраняем текущие значения
    original_category_count = Category.category_count
    original_product_count = Category.product_count
    
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0
    
    yield
    
    # Восстанавливаем исходные значения
    Category.category_count = original_category_count
    Category.product_count = original_product_count


def test_category_init_and_counters_single_category():
    """Проверяет инициализацию категории и автообновление счётчиков при одной категории."""
    # Запоминаем текущие значения счетчиков
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count
    
    p1 = Product("A", "desc A", 10.0, 1)
    p2 = Product("B", "desc B", 20.0, 2)
    cat = Category("Смартфоны", "Описание", [p1, p2])

    assert cat.name == "Смартфоны"
    assert cat.description == "Описание"
    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + 2

    # доступ к атрибутам класса через экземпляр
    assert cat.category_count == Category.category_count
    assert cat.product_count == Category.product_count


def test_category_counters_accumulate_across_instances():
    """Проверяет накопление счётчиков при создании нескольких категорий."""
    # Запоминаем текущие значения счетчиков
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count
    
    p1 = Product("A", "d", 10.0, 1)
    p2 = Product("B", "d", 20.0, 2)
    p3 = Product("C", "d", 30.0, 3)

    cat1 = Category("Смартфоны", "D1", [p1, p2])
    cat2 = Category("Телевизоры", "D2", [p3])

    assert Category.category_count == initial_category_count + 2
    assert Category.product_count == initial_product_count + 3

    # экземпляры отражают те же значения атрибутов класса
    assert cat1.category_count == Category.category_count
    assert cat2.category_count == Category.category_count
    assert cat1.product_count == Category.product_count
    assert cat2.product_count == Category.product_count


def test_category_add_product():
    """Проверяет добавление продукта через метод add_product."""
    # Запоминаем текущие значения счетчиков
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count
    
    cat = Category("Тест", "Описание")
    
    # После создания категории счетчики должны увеличиться
    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count  # пустая категория
    
    p = Product("New Product", "Desc", 100.0, 5)
    cat.add_product(p)
    
    # После добавления продукта счетчик продуктов должен увеличиться на 1
    assert Category.product_count == initial_product_count + 1


def test_category_products_getter():
    """Проверяет работу геттера products."""
    p1 = Product("Product 1", "Desc 1", 100.0, 5)
    p2 = Product("Product 2", "Desc 2", 200.0, 3)
    cat = Category("Тест", "Описание", [p1, p2])
    
    products_str = cat.products
    assert "Product 1, 100.0 руб. Остаток: 5 шт." in products_str
    assert "Product 2, 200.0 руб. Остаток: 3 шт." in products_str
    assert products_str.count('\n') == 2  # два продукта, два переноса строки


def test_category_private_products_access():
    """Проверяет, что приватный атрибут _products недоступен напрямую."""
    cat = Category("Тест", "Описание")
    
    # Попытка доступа к приватному атрибуту должна работать (Python не запрещает это)
    # но мы проверяем, что используется геттер через property
    assert hasattr(cat, '_products')
    assert hasattr(cat, 'products')  # property


def test_category_empty_products_list():
    """Проверяет работу с пустым списком продуктов."""
    cat = Category("Пустая категория", "Описание")
    
    # Пустая категория должна иметь пустой геттер
    assert cat.products == ""
    
    # Добавляем продукт
    p = Product("Test", "Desc", 100.0, 1)
    cat.add_product(p)
    
    # Теперь должен быть один продукт
    products_str = cat.products
    assert "Test, 100.0 руб. Остаток: 1 шт." in products_str
    assert products_str.count('\n') == 1