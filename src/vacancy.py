from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass


class Vacancy(BaseProduct):
    """ваканьсий"""

    name: str  # Название вокакнсии
    base_url: str  # ссылка
    description: str  # описание
    price: str  # цена

    def __init__(self, name, base_url, description, price):
        self.name = name
        self.__base_url = base_url
        self.description = description
        try:
            self.price = price
            raise TypeError
        except TypeError as e:
            print(e)
            print("Зарплата не указана")

    @classmethod
    def new_vacancy(cls, new_vacancy: dict):
        name = new_vacancy["name"]
        __base_url = new_vacancy["base_url"]
        description = new_vacancy["description"]
        price = new_vacancy["price"]
        return cls(name, __base_url, price, description)


    self.__base_url = "https://api.hh.ru/vacancies"

