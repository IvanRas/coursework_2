import unittest

from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):

    def test_initialization(self):
        vacancy = Vacancy(
            name="Разработчик Python",
            area="Москва",
            url="http://example.com/vacancy/1",
            salary_from="0",
            salary_to="120000",
            description="Заниматься разработкой на Python.",
        )

        self.assertEqual(vacancy.name, "Разработчик Python")
        self.assertEqual(vacancy.area, "Москва")
        self.assertEqual(vacancy.url, "http://example.com/vacancy/1")
        self.assertEqual(vacancy.salary_from, "0")
        self.assertEqual(vacancy.salary_to, "120000")
        self.assertEqual(vacancy.description, "Заниматься разработкой на Python.")

    def teST_srt_(self):
        """Проверяет работу метода __str__."""
        vacancy = Vacancy(
            name="Разработчик Python",
            area="Москва",
            url="http://example.com/vacancy/1",
            salary_from="0",
            salary_to="120000",
            description="Заниматься разработкой на Python.",
        )

        expected_str = "Разработчик Python, Москва, Зарплата от 0 до 120000, Ссылка: http://example.com/vacancy/1"
        self.assertEqual(str(vacancy), expected_str)

    def test_lt_method(self):
        """Проверяет правильность работы оператора <."""
        vacancy1 = Vacancy(
            name="Разработчик Python",
            area="Москва",
            url="http://example.com/vacancy/1",
            salary_from="0",
            salary_to="120000",
            description="Заниматься разработкой на Python.",
        )

        self.assertIsNone(vacancy1.validate())

        vacancy2 = Vacancy(
            name="Разработчик Python",
            area="Москва",
            url="http://example.com/vacancy/1",
            salary_from="0",
            salary_to="130000",
            description="Заниматься разработкой на Python.",
        )

        self.assertTrue(vacancy1 < vacancy2)
        self.assertFalse(vacancy2 < vacancy1)

    def test_validate_method(self):
        """Проверяет метод валидации."""
        valid_vacancy = Vacancy(
            "Разработчик", "Санкт-Петербург", "http://example.com/vacancy/2", "90000", "120000", "Описание"
        )
        self.assertIsNone(valid_vacancy.validate())

        invalid_vacancy_1 = Vacancy(
            "", "Санкт-Петербург", "http://example.com/vacancy/2", "90000", "12000", "Описание"
        )
        with self.assertRaises(ValueError) as context:
            invalid_vacancy_1.validate()
        self.assertEqual(str(context.exception), "Название и ссылка на вакансию обязательны.")

        invalid_vacancy_3 = Vacancy("Разработчик", "Санкт-Петербург", "", "90000", "12000", "Описание")
        with self.assertRaises(ValueError) as context:
            invalid_vacancy_3.validate()
        self.assertEqual(str(context.exception), "Название и ссылка на вакансию обязательны.")
