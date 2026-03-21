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
        self._products: List[Product] = products or []  # приватный список товаров

        # автоматическое обновление атрибутов класса
        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product: Product) -> None:
        """
        Добавление товара в категорию.

        :param product: Товар для добавления.
        :raises TypeError: если объект не Product или его наследник.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер продуктов в виде форматированной строки.

        :return: Строка вида "Название, X руб. Остаток: Y шт.\n" для каждого товара.
                 Для пустой категории — пустая строка.
        """
        if not self._products:
            return ""
        return "".join(f"{str(p)}\n" for p in self._products)

    def middle_price(self) -> float:
        """
        Подсчет среднего ценника всех товаров в категории.

        :return: Средняя цена товаров в категории.
             Возвращает 0, если в категории нет товаров.
        """
        try:
            if not self._products:
                return 0.0

            total_price = sum(product.price for product in self._products)
            return total_price / len(self._products)
        except ZeroDivisionError:
            return 0.0

    def __str__(self) -> str:
        """
        Строковое представление категории.

        :return: "Название категории, количество продуктов: N шт."
                 где N — сумма quantity всех товаров.
        """
        total_quantity = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator:
    """Итератор для категории товаров."""

    def __init__(self, category: Category) -> None:
        """
        Инициализация итератора.

        :param category: Объект категории.
        """
        self.category = category
        self.index = 0

    def __iter__(self):
        """Возвращает сам итератор."""
        return self

    def __next__(self) -> Product:
        """
        Возвращает следующий товар по списку категории.

        :raises StopIteration: когда товары закончились.
        """
        if self.index >= len(self.category._products):
            raise StopIteration
        product = self.category._products[self.index]
        self.index += 1
        return product
