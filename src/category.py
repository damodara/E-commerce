from typing import List, Optional

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
    products: List[Product]

    # атрибуты класса (общие для всех объектов)
    category_count = 0
    product_count = 0

    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ) -> None:
        """
        Инициализация категории.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров в категории.
        """
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # автоматическое обновление атрибутов класса
        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product) -> None:
        """
        Добавление товара в категорию.

        :param product: Товар для добавления.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        self.products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> List[Product]:
        """Геттер для списка товаров."""
        return self._products

    @products.setter
    def products(self, value: List[Product]) -> None:
        """Сеттер для списка товаров."""
        self._products = value

    def __str__(self) -> str:
        """
        Строковое представление категории.

        :return: Строка с информацией о категории.
        """
        if not self.products:
            return f"{self.name}, {self.description}"

        product_names = [product.name for product in self.products]
        return f"{self.name}, {self.description}, товары: {', '.join(product_names)}"

    def __iter__(self):
        """Итератор по товарам категории."""
        return CategoryIterator(self.products)


class CategoryIterator:
    """Итератор для категории товаров."""

    def __init__(self, products: List[Product]) -> None:
        """
        Инициализация итератора.

        :param products: Список товаров.
        """
        self.products = products
        self.index = 0

    def __iter__(self):
        """Возвращает сам итератор."""
        return self

    def __next__(self) -> Product:
        """Возвращает следующий товар."""
        if self.index >= len(self.products):
            raise StopIteration
        product = self.products[self.index]
        self.index += 1
        return product
