from typing import Dict, Union


class Book:
    """Класс, представляющий книгу в библиотеке"""

    def __init__(self, book_id: int, title: str, author: str, year: int):
        """
        Инициализация книги

        :param book_id: Уникальный id книги
        :param title: Название книги
        :param author: Автор книги
        :param year: Год выпуска книги
        """

        self.book_id: int = book_id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = "в наличии"

    def convert_to_dict(self) -> Dict[str, Union[int, str]]:
        """Преобразование книги в словарь для сохранения в JSON"""
        return {
            'id': self.book_id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

    @staticmethod
    def get_from_dict(data) -> 'Book':
        """Создание книги из словаря"""
        book = Book(data['id'], data['title'], data['author'], data['year'])
        book.status = data['status']
        return book

    def __str__(self) -> str:
        """Вывод информации о книге"""
        return f"ID: {self.book_id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"
