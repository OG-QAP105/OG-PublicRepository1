"""
Здесь и __init__, и is_available — это методы. По умолчанию первым аргументом во все методы класса
подается self — именно так метод получает доступ к экземпляру класса.
Мы рассмотрим исключения позже в течение курса. При этом, чтобы вызвать исполнение метода,
передавать self уже не нужно:
"""

class Product:
    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


eggs = Product("eggs", "food", 5)

print(eggs.is_available())
print(eggs.name, eggs.category, eggs.quantity_in_stock)
