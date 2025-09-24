from typing import List

from src.product import Product


class Category:
    name: str
    description: str
    products: List[Product]
    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products