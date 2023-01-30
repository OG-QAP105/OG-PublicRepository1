"""
Представим, что нам нужно создать множество однотипных объектов. Например, у нас есть пользователи
нашего сервиса PetFriends (вы же помните о прототипе социальной сети для проекта «Дом Питомца»?).
Мы хотим хранить данные о них, плюс дополнительно хранить предлагаемые товары для питомцев,
а кроме этого — соответствующие функции, которые рассчитывают, например, доступность.
"""

user_peter = {
    "name": "Peter",
    "email": "peterrobertson@mail.com",
    "created_at": "2019-05-05",
    "is_email_verified": True,
    "purchases": ["Egg", "Spam", "Hat", "Knife", "Shield", "Book of Knight secrets"],
}

user_julia = {
    "name": "Julia Donaldson",
    "email": "juliadonaldson@mail.com",
    "created_at": "2019-06-13",
    "is_email_verified": True,
    "purchases": ["Egg", "Spam", "Magic Brush"],
}

product_eggs = {
    "name": "Egg",
    "category": "food",
    "is_available": False,
    "quantity_in_stock": 1,
    "vendor": "Dark Knight LTD",
    "manager": "William The Conqueror",
}


def is_product_available(product):
    return True if (product_eggs["name"] == "Egg") and (product_eggs["quantity_in_stock"] > 0) else False


print(is_product_available("Egg"))