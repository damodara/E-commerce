from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Абстрактный метод инициализации продукта.

        :param name: Название товара.
        :param description: Описание товара.
        :param price: Цена товара.
        :param quantity: Количество товара на складе.
        """
        pass

    @abstractmethod
    def get_total_value(self) -> float:
        """
        Абстрактный метод для получения общей стоимости товара.

        :return: Общая стоимость (цена * количество).
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Абстрактный метод строкового представления.

        :return: Строковое представление продукта.
        """
        pass

    def is_available(self) -> bool:
        """
        Проверка доступности товара.

        :return: True, если товар есть в наличии.
        """
        return self.quantity > 0

    def get_info(self) -> dict:
        """
        Получение информации о товаре.

        :return: Словарь с информацией о товаре.
        """
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
            "total_value": self.get_total_value(),
            "available": self.is_available(),
        }
