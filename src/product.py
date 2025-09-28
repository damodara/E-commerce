class Product:
    """Модель товара в каталоге."""

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация товара.

        :param name: Название товара.
        :param description: Описание товара.
        :param price: Цена товара.
        :param quantity: Количество товара на складе.
        """
        self.name = name
        self.description = description
        self._price = price  # приватный атрибут
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер для приватного атрибута цены с проверкой.

        :param value: Новое значение цены.
        """
        if value > 0:
            self._price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict) -> 'Product':
        """
        Класс-метод для создания продукта из словаря.

        :param product_data: Словарь с данными продукта.
        :return: Экземпляр класса Product.
        """
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @classmethod
    def new_product_with_duplicate_check(cls, product_data: dict, existing_products: list) -> 'Product':
        """
        Класс-метод для создания продукта с проверкой дубликатов.

        :param product_data: Словарь с данными продукта.
        :param existing_products: Список существующих продуктов для проверки дубликатов.
        :return: Экземпляр класса Product или обновленный существующий продукт.
        """
        # Поиск дубликата по имени
        for existing_product in existing_products:
            if existing_product.name.lower() == product_data['name'].lower():
                # Складываем количество
                existing_product.quantity += product_data['quantity']
                # Выбираем более высокую цену
                if product_data['price'] > existing_product.price:
                    existing_product.price = product_data['price']
                return existing_product
        
        # Если дубликат не найден, создаем новый продукт
        return cls.new_product(product_data)