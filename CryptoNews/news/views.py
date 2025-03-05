import os
from dotenv import load_dotenv #чтобы токен был скрыт

from django.shortcuts import render
import requests

from .models import Post


load_dotenv()
AUTH_TOKEN = os.getenv('auth_token')


def main(request):
    # url = 'https://cryptopanic.com/api/free/v1/posts/'
    # params = {
    #     'auth_token': AUTH_TOKEN
    # }
    #
    # news_big = requests.get(url=url, params=params).json()['results']
    #
    # for new in news_big:
    #     Post.objects.create(title=new['title'], content=new['title'], source=new['url'])

    data = {'news': Post.objects.all(), 'title': 'CryptoNews'}
    return render(request, 'news/base.html', data)
