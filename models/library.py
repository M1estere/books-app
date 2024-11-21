from .book import Book
import json
import os
from typing import Dict, List, Union


class Library:
    """Класс, представляющий библиотеку с набором книг"""

    def __init__(self, filename: str = 'library.json'):
        """
        Инициализация библиотеки

        :param filename: Имя файла для хранения данных о книгах
        """
        self.books: Dict[int, Book] = {}
        self.next_id: int = 1
        self.filename: str = filename

        self.load_books()

    def load_books(self) -> None:
        """Загрузка книг из файла JSON"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for book_data in data:
                    book = Book.get_from_dict(book_data)
                    self.books[book.book_id] = book
                    self.next_id = max(self.next_id, book.book_id + 1)

    def save_books(self) -> None:
        """Сохранение книг в файл JSON"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.convert_to_dict() for book in self.books.values()], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавление новой книги в библиотеку

        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        """
        book = Book(self.next_id, title, author, year)
        self.books[self.next_id] = book
        self.next_id += 1
        self.save_books()

        print(f"Книга '{title}' добавлена с ID {book.book_id}")

    def remove_book(self, book_id: int) -> None:
        """Удаление книги из библиотеки по ID

        :param book_id: Уникальный id книги
        :raises ValueError: Если книга с данным ID не найдена
        """
        if book_id in self.books:
            del self.books[book_id]
            self.save_books()
            print(f"Книга с ID {book_id} удалена.")
        else:
            raise ValueError("Ошибка: Книга с таким ID не найдена")

    def search_books(self, query: Union[str, int]) -> List[Book]:
        """Поиск книг по названию, автору или году

        :param query: Строка для поиска
        :return: Список найденных книг
        """
        query = str(query)
        results = [book for book in self.books.values() if
                   query.lower() in book.title.lower() or
                   query.lower() in book.author.lower() or
                   str(book.year) == str(query)]

        return results

    def display_books(self) -> None:
        """Отображение всех книг в библиотеке"""
        if not self.books:
            print("Библиотека пуста")
        else:
            for book in self.books.values():
                print(book)

    def change_status(self, book_id: int, new_status: str) -> None:
        """Изменение статуса книги

        :param book_id: Уникальный идентификатор книги
        :param new_status: Новый статус книги ('в наличии' или 'выдана')
        :raises ValueError: Если книга с данным ID не найдена или статус некорректен
        """
        if book_id in self.books:
            if new_status in ["в наличии", "выдана"]:
                self.books[book_id].status = new_status
                self.save_books()
                print(f"Статус книги с ID {book_id} изменен на '{new_status}'")
            else:
                raise ValueError("Ошибка: Некорректный статус. Доступные статусы: 'в наличии', 'выдана'")
        else:
            raise ValueError("Ошибка: Книга с таким ID не найдена")
