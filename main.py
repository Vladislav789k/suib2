# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ye1HD8XDW02CQ5T129hJC3X17LuXnnL9
"""

import pandas as pd

# Создание данных студентов
students = [
    {
        "Фамилия": "Иванов",
        "Имя": "Иван",
        "Дата рождения": "2000-01-15",
        "Зачетка": [
            {"Предмет": "Математика", "Дата экзамена": "2024-05-20", "ФИО преподавателя": "Петров Петр Петрович"},
            {"Предмет": "Физика", "Дата экзамена": "2024-06-10", "ФИО преподавателя": "Иванова Анна Сергеевна"},
            {"Предмет": "Информатика", "Дата экзамена": "2024-05-25", "ФИО преподавателя": "Сидоров Игорь Владимирович"}
        ]
    },
    {
        "Фамилия": "Петрова",
        "Имя": "Анна",
        "Дата рождения": "2001-03-22",
        "Зачетка": [
            {"Предмет": "Математика", "Дата экзамена": "2024-05-21", "ФИО преподавателя": "Петров Петр Петрович"},
            {"Предмет": "Физика", "Дата экзамена": "2024-06-11", "ФИО преподавателя": "Иванова Анна Сергеевна"},
            {"Предмет": "Информатика", "Дата экзамена": "2024-05-26", "ФИО преподавателя": "Сидоров Игорь Владимирович"}
        ]
    },
    {
        "Фамилия": "Сидоров",
        "Имя": "Алексей",
        "Дата рождения": "2002-07-18",
        "Зачетка": [
            {"Предмет": "Математика", "Дата экзамена": "2024-05-22", "ФИО преподавателя": "Петров Петр Петрович"},
            {"Предмет": "Физика", "Дата экзамена": "2024-06-12", "ФИО преподавателя": "Иванова Анна Сергеевна"},
            {"Предмет": "Информатика", "Дата экзамена": "2024-05-27", "ФИО преподавателя": "Сидоров Игорь Владимирович"}
        ]
    }
]

# Создание DataFrame для отображения данных
data = {
    "ФИО": [f"{student['Фамилия']} {student['Имя']}" for student in students],
    "Дата рождения": [student["Дата рождения"] for student in students]
}

df = pd.DataFrame(data)

# Вывод таблицы
print(df)

# Для более удобного вывода в Jupyter Notebook можно использовать display(df)
# from IPython.display import display
# display(df)