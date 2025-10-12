class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs) -> None:
        """
        Инициализация с логированием.

        :param args: Позиционные аргументы.
        :param kwargs: Именованные аргументы.
        """
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        """
        Представление объекта для отладки.

        :return: Строковое представление объекта.
        """
        class_name = self.__class__.__name__
        args_str = ", ".join([repr(arg) for arg in self._get_init_args()])
        return f"{class_name}({args_str})"

    def _get_init_args(self) -> list:
        """Получение аргументов инициализации для логирования."""
        return [self.name, self.description, self.price, self.quantity]

    def _log_creation(self, *args) -> None:
        """Метод для логирования создания объекта."""
        class_name = self.__class__.__name__
        args_str = ", ".join([repr(arg) for arg in args])
        print(f"{class_name}({args_str})")
