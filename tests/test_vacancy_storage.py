import json
import os
import unittest
from tempfile import NamedTemporaryFile

from src.vacancy import Vacancy
from src.vacancy_storage import JSONVacancyStorage


class TestJSONVacancyStorage(unittest.TestCase):
    def setUp(self):
        """Создание временного файла для тестов"""
        self.temp_file = NamedTemporaryFile()
        self.temp_file.close()
        self.storage = JSONVacancyStorage(self.temp_file.name)

    def test_add_vacancy(self):
        """Тестирование добавления вакансии"""
        vacancy = Vacancy(
            "Программист", "Москва", "http://example.com/vacancy1", "100000", "150000", "Описание вакансии"
        )
        self.storage.add_vacancy(vacancy)

        with open(self.temp_file.name, "r", encoding="utf-8") as file:
            vacancies = json.load(file)

        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]["title"], "Программист")
        self.assertEqual(vacancies[0]["area"], "Москва")

    def test_get_vacancies(self):
        """Тестирование получения вакансий"""
        vacancy1 = Vacancy(
            "Программист", "Москва", "http://example.com/vacancy1", "100000", "150000", "Описание вакансии"
        )
        vacancy2 = Vacancy(
            "Дизайнер",
            "Санкт-Петербург",
            "http://example.com/vacancy2",
            "80000",
            "120000",
            "Описание вакансии дизайнера",
        )
        self.storage.add_vacancy(vacancy1)
        self.storage.add_vacancy(vacancy2)
        vacancies = self.storage.get_vacancies("дизайнер")
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0].name, "Дизайнер")

    def test_remove_vacancy(self):
        """Тестирование удаления вакансии"""
        vacancy = Vacancy(
            "Программист", "Москва", "http://example.com/vacancy1", "100000", "150000", "Описание вакансии"
        )
        self.storage.add_vacancy(vacancy)

        self.storage.remove_vacancy(vacancy)

        with open(self.temp_file.name, "r", encoding="utf-8") as file:
            vacancies = json.load(file)

        self.assertEqual(len(vacancies), 0)

    def tearDown(self):
        """Удаление временного файла после тестов"""
        os.unlink(self.temp_file.name)
