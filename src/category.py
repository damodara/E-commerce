from typing import List

from src.product import Product


class Category:
    name: str
    description: str
    products: List[Product]

    # атрибуты класса (общие для всех объектов)
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products

        # автоматическое обновление атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products)