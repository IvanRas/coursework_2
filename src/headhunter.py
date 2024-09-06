from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass


class HeadHunter:

    def __init__(self, name, description, price, quantity):
        pass

