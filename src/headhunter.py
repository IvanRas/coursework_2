from abc import ABC, abstractmethod
from email.parser import Parser

import requests


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass


class HeadHunter:

    name: str  # название продукта
    price: str  # цена  продукта
    url: str
    description: str  # описание  продукта

    def __init__(self, name, description, price, url):
        self.name = name
        self.description = description
        self.url = url
        self.price = price

    def __str__(self):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1