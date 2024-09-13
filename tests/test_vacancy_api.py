import unittest
from unittest.mock import Mock, patch

from src.vacancy_api import HHVacancyAPI


class TestHHVacancyAPI(unittest.TestCase):

    @patch("requests.get")
    def test_fetch_area_id(self, mock_get):
        # Подготовим фиктивные данные, чтобы имитировать ответ API для поиска id городов
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "areas": [
                    {"name": "Москва", "id": 1, "areas": []},
                    {
                        "name": "Санкт-Петербург",
                        "id": 2,
                        "areas": [{"name": "Центральный", "id": 3}, {"name": "Петроградский", "id": 4}],
                    },
                ]
            }
        ]
        mock_get.return_value = mock_response

        api = HHVacancyAPI()

        # Тестируем поиск по области "Москва"
        area_id = api._HHVacancyAPI__fetch_area_id("Москва")
        self.assertEqual(area_id, 1)

        # Тестируем поиск по области "Центральный"
        area_id = api._HHVacancyAPI__fetch_area_id("Центральный")
        self.assertEqual(area_id, 3)

        # Тестируем поиск по области, которая не существует
        area_id = api._HHVacancyAPI__fetch_area_id("Неизвестный Город")
        self.assertIsNone(area_id)

    @patch("requests.get")
    def test_fetch_vacancies(self, mock_get):
        # Подготовим фиктивные данные для вакансий
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"items": [{"id": 1, "name": "Вакансия 1"}, {"id": 2, "name": "Вакансия 2"}]}
        mock_get.return_value = mock_response

        api = HHVacancyAPI()

        # Тест получения вакансий
        vacancies = api.fetch_vacancies("разработчик", "Москва", 0, 10)
        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]["name"], "Вакансия 1")

        # Проверяем отрицательный сценарий на статус 404
        mock_response.status_code = 404
        vacancies = api.fetch_vacancies("разработчик", "Неизвестный Город", 0, 10)
        self.assertEqual(vacancies, [])