import os

from src.vacancy_api import HHVacancyAPI
from src.vacancy_storage import JSONVacancyStorage
from src.vacancy import Vacancy


def main() -> None:
    """Функция взаимодействия с пользователем"""
