class Vacancy:
    """класс для описания вваканьсий"""

    name: str  # Название вокакнсии
    area: str  # населенный пункт (город, регион, и т.д.)
    url: str  # ссылка на ваканьсию
    description: str  # описание
    salary_from: float | str  # зарплата от,,,
    salary_to: float | str  # зарплата до ,,,

    __slots__ = ("name", "area", "url", "salary_from", "salary_to", "description")

    def __init__(self, name, area, url, description, salary_from, salary_to) -> None:
        self.name = name
        self.area = area
        self.url = url
        self.description = description
        self.salary_from: str = salary_from if salary_from else "0"
        self.salary_to: str = salary_to if salary_to else "0"
        # try:
        #     self.price = price
        #     raise TypeError
        # except TypeError as e:
        #     print(e)
        #     print("Зарплата не указана")

    def __str__(self) -> str:
        return f"{self.name}, {self.area}, Зарплата от {self.salary_from} до {self.salary_to}, Ссылка {self.url}"

    # def __lt__(self, other: "Vacancy") -> str:
    #     if int(self.salary_to) < int(other.salary_to):
    #         return f"выгодное предложение с зарплатой {other.salary_to}"
    #     else:
    #         return f"выгодное предложение с зарплатой {self.salary_to}"

    def __lt__(self, other: "Vacancy") -> bool:
        return int(self.salary_to) < int(other.salary_to)

    def validate(self) -> None:
        if not self.name or not self.url:
            raise ValueError("Название и ссылка на вакансию обязательны.")
