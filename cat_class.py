"""
Создадим конструктор класса Cat со следующими параметрами: имя, пол, возраст:
"""
class Cat:

    species = "кошка"

    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age


