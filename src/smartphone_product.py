from src.product import Product


class Smartphone(Product):
    """Модель смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Инициализация смартфона.

        :param name: Название смартфона.
        :param description: Описание смартфона.
        :param price: Цена смартфона.
        :param quantity: Количество на складе.
        :param efficiency: Производительность.
        :param model: Модель.
        :param memory: Объем памяти.
        :param color: Цвет.
        """
        # Сохраняем все аргументы для логирования
        self._all_init_args = [
            name,
            description,
            price,
            quantity,
            efficiency,
            model,
            memory,
            color,
        ]

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

        # Логируем создание смартфона
        self._log_creation(
            name, description, price, quantity, efficiency, model, memory, color
        )

    def _get_init_args(self) -> list:
        """Переопределение для корректного логирования."""
        return self._all_init_args

    def get_specifications(self) -> dict:
        """
        Получение технических характеристик.

        :return: Словарь с характеристиками.
        """
        base_info = self.get_info()
        base_info.update(
            {
                "efficiency": self.efficiency,
                "model": self.model,
                "memory": self.memory,
                "color": self.color,
            }
        )
        return base_info
