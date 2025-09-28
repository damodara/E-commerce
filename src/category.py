from typing import List

from src.product import Product


class Category:
    """Модель категории товаров.

    Атрибуты класса:
        category_count: Общее количество созданных категорий.
        product_count: Общее количество товаров во всех созданных категориях
                       (сумма длин списков products при инициализации).
    """

    name: str
    description: str

    # атрибуты класса (общие для всех объектов)
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product] = None):
        """
        Инициализация категории.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров, относящихся к категории.
        """
        self.name = name
        self.description = description
        self._products = products or []  # приватный атрибут

        # автоматическое обновление атрибутов класса
        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product: Product) -> None:
        """
        Добавление продукта в категорию.

        :param product: Продукт для добавления.
        """
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер для приватного атрибута products.
        
        :return: Строка со всеми продуктами в формате "Название продукта, X руб. Остаток: X шт.\n"
        """
        result = ""
        for product in self._products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result