from celery import shared_task
import requests


@shared_task
def fetch_api_data():
    # Пример API-запроса
    response = requests.get('https://api.example.com/data')

    if response.status_code == 200:
        # Обработать данные и сохранить в базе данных или выполнить другие действия
        data = response.json()
        print("Полученные данные:", data)
    else:
        print("Ошибка при запросе:", response.status_code)