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
            result += str(product) + "\n"  # Используем __str__ продукта
        return result

    def __str__(self) -> str:
        """
        Строковое представление категории.

        :return: Строка в формате "Название категории, количество продуктов: X шт."
        """
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator:
    """Итератор для перебора товаров в категории."""

    def __init__(self, category: Category):
        """
        Инициализация итератора.

        :param category: Объект категории для итерации.
        """
        self.category = category
        self.index = 0

    def __iter__(self):
        """Возвращает сам объект как итератор."""
        return self

    def __next__(self) -> Product:
        """
        Возвращает следующий продукт в категории.

        :return: Следующий продукт.
        :raises StopIteration: Когда продукты закончились.
        """
        if self.index < len(self.category._products):
            product = self.category._products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
