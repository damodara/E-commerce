from src.base_product import BaseProduct
from src.product import Product


class Order(BaseProduct):
    """Модель заказа."""

    def __init__(self, product: Product, quantity: int):
        """
        Инициализация заказа.

        :param product: Товар для заказа.
        :param quantity: Количество товара в заказе.
        """
        self.product = product
        self.quantity = quantity
        self.name = f"Заказ {product.name}"
        self.description = f"Заказ товара: {product.description}"
        self._price = product.price

    @property
    def price(self) -> float:
        """Геттер для цены товара в заказе."""
        return self._price

    def get_total_value(self) -> float:
        """
        Получение общей стоимости заказа.

        :return: Общая стоимость (цена товара * количество в заказе).
        """
        return self.product.price * self.quantity

    def __str__(self) -> str:
        """
        Строковое представление заказа.

        :return: Строка в формате "Заказ: название товара, количество: X, стоимость: X руб."
        """
        return f"Заказ: {self.product.name}, количество: {self.quantity}, стоимость: {self.get_total_value()} руб."

    def is_available(self) -> bool:
        """
        Проверка возможности выполнения заказа.

        :return: True, если товара достаточно на складе.
        """
        return self.product.quantity >= self.quantity

    def execute(self) -> bool:
        """
        Выполнение заказа (списание товара со склада).

        :return: True, если заказ выполнен успешно, False - если товара недостаточно.
        """
        if self.is_available():
            self.product.quantity -= self.quantity
            return True
        return False
