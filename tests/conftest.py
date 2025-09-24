import pytest

from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counters():
    # сбрасываем счётчики перед каждым тестом
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0
