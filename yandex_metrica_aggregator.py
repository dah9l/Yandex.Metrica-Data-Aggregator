import requests
import sqlite3
import json

# API-ключ Яндекс.Метрики
api_key = "YOUR_API_KEY"

# URL-адрес API Яндекс.Метрики
api_url = "https://api-metrika.yandex.ru/stat/v1/data"

# Создаем соединение с базой данных
conn = sqlite3.connect("metrika_data.db")
cursor = conn.cursor()

# Создаем таблицу, если она не существует
cursor.execute("""
    CREATE TABLE IF NOT EXISTS metrika_data (
        date DATE,
        visits INTEGER,
        pageviews INTEGER,
        bounce_rate REAL,
        avg_visit_duration REAL
    )
""")

# Определяем параметры запроса к API
params = {
    "id": "YOUR_COUNTER_ID",
    "metrics": "ym:s:visits,ym:s:pageviews,ym:s:bounceRate,ym:s:avgVisitDuration",
    "dimensions": "ym:s:date",
    "sort": "ym:s:date",
    "limit": 100
}

# Добавляем API-ключ к параметрам
params["oauth_token"] = api_key

# Отправляем запрос к API
response = requests.get(api_url, params=params)

# Обрабатываем ответ от API
if response.status_code == 200:
    data = json.loads(response.content)
    for row in data["data"]:
        date = row["dimensions"][0]["name"]
        visits = row["metrics"][0]["values"][0]
        pageviews = row["metrics"][1]["values"][0]
        bounce_rate = row["metrics"][2]["values"][0]
        avg_visit_duration = row["metrics"][3]["values"][0]

        # Добавляем данные в базу
        cursor.execute("""
            INSERT INTO metrika_data (date, visits, pageviews, bounce_rate, avg_visit_duration)
            VALUES (?, ?, ?, ?, ?)
        """, (date, visits, pageviews, bounce_rate, avg_visit_duration))

    # Сохраняем изменения в базе
    conn.commit()
else:
    print("Ошибка при получении данных от API:", response.status_code)

# Закрываем соединение с базой
conn.close()
