import requests     # Импортируем модуль requests для выполнения HTTP-запросов
import json     # Импортируем модуль json для работы с JSON-данными
import pprint       # Импортируем модуль pprint для удобного форматирования вывода

# Выполняем GET-запрос к API, чтобы получить данные о текущем курсе USD
result = requests.get("https://open.er-api.com/v6/latest/USD")
data = json.loads(result.text)      # Преобразуем полученный текст в формат JSON для удобной работы с данными
p = pprint.PrettyPrinter(indent=4)    # Создаем экземпляр PrettyPrinter с отступом 4 пробела для форматированного вывода данных

p.pprint(data)   # Выводим отформатированные данные JSON