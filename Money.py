import requests     # Импортируем модуль requests для выполнения HTTP-запросов
import json     # Импортируем модуль json для работы с JSON-данными
from tkinter import *   # Импортируем все из модуля tkinter для создания графического интерфейса
from tkinter import messagebox as mb    # Импортируем модуль для работы с всплывающими сообщениями
from tkinter import ttk     # Импортируем модуль ttk из библиотеки tkinter для использования виджетов с расширенными стилями и функциями


def update_t_label(event):
    code = t_combobox.get()   # Получаем выбранный код валюты из целевого выпадающего списка (combobox)
    name = cur[code]    # Получаем название валюты из словаря cur
    t_label.config(text=name)   # Обновляем текст целевой метки на название валюты


def update_b_label(event):
    code = b_combobox.get()   # Получаем выбранный код валюты из базового выпадающего списка (combobox)
    name = cur[code]    # Получаем название валюты из словаря cur
    b_label.config(text=name)   # Обновляем текст базовой метки на название валюты


def exchange():
    t_code = t_combobox.get()  # Получаем выпадающий список кода валюты.
    b_code = b_combobox.get()
    if t_code and b_code:    # Проверяем, что пользователь ввел код валюты
        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{b_code}")    # Отправляем GET-запрос на API для получения актуальных курсов валют
            response.raise_for_status()     # Если запрос не успешен (например, сервер вернул ошибку), выбрасываем исключение
            data = response.json()      # Преобразуем полученные JSON-данные в словарь Python
            if t_code in data["rates"]:   # Проверяем, есть ли введенный код валюты в данных, полученных от API
                exchange_rate = data["rates"][t_code]     # Если код валюты найден, получаем курс обмена
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}")   # Отображаем курс обмена
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена!")   # Если код валюты не найден, отображаем сообщение об ошибке
        except Exception as e:
            mb.showerror("Ошибка" f"Произошла ошибка: {e}.")     # Если произошла ошибка, отображаем сообщение об ошибке
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")      # Если пользователь не ввел код валюты, показываем предупреждение

# Словарь с кодами валют и их названиями
cur = {'RUB': 'Российский рубль',
       'EUR': 'Евро',
       'GBP': 'Британский фунт стерлингов',
       'JPY': 'Японская йена',
       'CNY': 'Китайский юань',
       'KZT': 'Казахский тенге',
       'UZS': 'Узбекский сум',
       'CHF': 'Швейцарский франк',
       'AED': 'Дирхам ОАЭ',
       'CAD': 'Канадский доллар',
       'USD': 'Американский доллар',}

window = Tk()   # Создаем главное окно приложения
window.title("Курсы обмена валют")   # Устанавливаем заголовок окна
window.geometry("360x300")   # Задаем размеры окна

Label(text="Базовая валюта").pack(padx=10, pady=10)     # Добавляем метку с текстом, базовой валюты
b_combobox = ttk.Combobox(values=list(cur.keys()))     # Создаем выпадающий список с значениями валют из списка cur
b_combobox.pack(padx=10, pady=10)       # Размещаем комбобокс (выпадающий список) на окне с отступами по оси X и Y
b_combobox.bind("<<ComboboxSelected>>", update_b_label) # Привязываем функцию обновления базовой метки к событию выбора элемента в комбобоксе

b_label = ttk.Label()   # Создаем метку для отображения названия базовой валюты
b_label.pack(padx=10, pady=10)  # Размещаем метку на окне с отступами по оси X и Y

Label(text="Целевая валюта").pack(padx=10, pady=10)     # Добавляем метку с текстом, целевой валюты
t_combobox = ttk.Combobox(values=list(cur.keys()))     # Создаем выпадающий список с значениями валют из списка cur
t_combobox.pack(padx=10, pady=10)     # Размещаем комбобокс (выпадающий список) на окне с отступами по оси X и Y
t_combobox.bind("<<ComboboxSelected>>", update_t_label) # Привязываем функцию обновления целевой метки к событию выбора элемента в комбобоксе

t_label = ttk.Label()   # Создаем метку для отображения названия целевой валюты
t_label.pack(padx=10, pady=10)  # Размещаем метку на окне с отступами по оси X и Y

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)      # Создаем кнопку, при нажатии на которую будет выполняться функция exchange

window.mainloop()   # Запускаем главный цикл