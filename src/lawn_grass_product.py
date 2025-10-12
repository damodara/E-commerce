from src.product import Product


class LawnGrass(Product):
    """Модель газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """
        Инициализация газонной травы.

        :param name: Название травы.
        :param description: Описание травы.
        :param price: Цена травы.
        :param quantity: Количество на складе.
        :param country: Страна-производитель.
        :param germination_period: Срок прорастания.
        :param color: Цвет травы.
        """
        # Сохраняем все аргументы для логирования
        self._all_init_args = [
            name,
            description,
            price,
            quantity,
            country,
            germination_period,
            color,
        ]

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

        # Логируем создание газонной травы
        self._log_creation(
            name, description, price, quantity, country, germination_period, color
        )

    def _get_init_args(self) -> list:
        """Переопределение для корректного логирования."""
        return self._all_init_args

    def get_growing_info(self) -> dict:
        """
        Получение информации о выращивании.

        :return: Словарь с информацией о выращивании.
        """
        base_info = self.get_info()
        base_info.update(
            {
                "country": self.country,
                "germination_period": self.germination_period,
                "color": self.color,
            }
        )
        return base_info
