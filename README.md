
### E-commerce (ООП, вводное задание)

Небольшой учебный проект для практики основ ООП на Python: модели `Product` (товар) и `Category` (категория товаров) с инициализацией и атрибутами класса (счётчики).

### Структура проекта
- `src/product.py` — класс `Product` с полями `name`, `description`, `price`, `quantity`.
- `src/category.py` — класс `Category` с полями `name`, `description`, `products` и атрибутами класса:
  - `category_count` — количество созданных категорий,
  - `product_count` — суммарное количество товаров во всех категориях (сумма длин списков `products` при инициализации).
- `main.py` — пример использования.
- `tests/` — тесты `pytest`, `conftest.py` содержит фикстуры.

### Требования
- Python 3.13 (проект создан под эту версию; подойдёт 3.11+ при необходимости).
- Рекомендуется использовать виртуальное окружение.


### Как это работает
- `Product.__init__(name, description, price, quantity)` — сохраняет параметры в атрибутах экземпляра.
- `Category.__init__(name, description, products)`:
  - сохраняет переданные значения в атрибутах экземпляра,
  - увеличивает `Category.category_count` на 1,
  - увеличивает `Category.product_count` на `len(products)`.

Доступ к счётчикам возможен как через класс (`Category.product_count`), так и через экземпляр (`category.product_count`), так как это атрибуты класса.
