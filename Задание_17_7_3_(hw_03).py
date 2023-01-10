# -*- coding: utf-8 -*-
"""ЗАДАНИЕ_17_7_3_(HW_03).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10P1MbeeJjdm60zGJYbrZVYaUgsvYuChb
"""

# Набор эффективных функций
import operator

# Распределение процентных ставок по вкладам в различных банках:
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Банк с максимальной процентной ставкой:
max_bank = max(per_cent.items(), key=operator.itemgetter(1))[0]

# Список процентных ставок:
list_per_cent = list(per_cent.values())

# Сумма депозита:
print()
money = float(input(">>> Введите сумму, которую Вы планируете положить под проценты : "))

# Накопленные средства за год вклада в каждом из банков:
deposit = [round((proc * money) / 100, 2) for proc in list_per_cent]

# Максимальная сумма депозита:
max_deposit = max(deposit)

# Результат:
print("\n    Максимальная сумма, которую Вы можете заработать на депозит:", max_deposit, "руб.", '( банк "',max_bank,'"',')')