import abc
import json
import os
from typing import List

from src.vacancy import Vacancy


class AbstractVacancyStorage(abc.ABC):
    """Абстрактный класс для работы с файлами"""

    @abc.abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавление вакансии в файл"""
        pass

    @abc.abstractmethod
    def get_vacancies(self, criterion: str) -> List[Vacancy]:
        """Получение вакансий по критериям"""
        pass

    @abc.abstractmethod
    def remove_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии из файла"""
        pass


class JSONVacancyStorage(AbstractVacancyStorage):
    """Класс для работы с JSON-файлом"""

    def __init__(self, filename: str) -> None:
        self.filename: str = filename

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавление вакансии в JSON файл"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                vacancies = json.load(file)
        else:
            vacancies = []

        vacancies.append(vacancy.__dict__)
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def get_vacancies(self, criterion: str) -> List[Vacancy]:
        """Получение вакансий по критерию"""
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
            return [Vacancy(**job) for job in vacancies if criterion.lower() in str(job["description"]).lower()]

    def remove_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии из JSON файла"""
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            vacancies = json.load(file)

            vacancies = [job for job in vacancies if not (job["name"] == vacancy.name and job["url"] == vacancy.url)]

            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(vacancies, file)
