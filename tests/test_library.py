# python -m unittest test_library.py -v

import unittest
from models.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Создание библиотеки для тестов"""
        self.library = Library('test_library.json')

    def test_add_book(self):
        """Добавление книги"""
        self.library.add_book("Test Book", "Test Author", 2023)
        self.assertEqual(len(self.library.books), 1)

    def test_remove_book(self):
        """Удаление книги"""
        self.library.add_book("Test Book", "Test Author", 2023)
        book_id = list(self.library.books.keys())[0]
        self.library.remove_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_remove_nonexistent_book(self):
        """Удаление несуществующей книги"""
        initial_count = len(self.library.books)
        with self.assertRaises(ValueError) as context:
            self.library.remove_book(999)

        self.assertEqual(str(context.exception), "Ошибка: Книга с таким ID не найдена")
        self.assertEqual(len(self.library.books), initial_count)

    def test_search_books(self):
        """Поиск книг"""
        self.library.add_book("Test Book", "Test Author", 2023)
        results = self.library.search_books("Test Book")
        self.assertEqual(len(results), 1)

    def test_search_books_by_author(self):
        """Поиск по автору"""
        self.library.add_book("Another Book", "Test Author", 2023)
        results = self.library.search_books("Test Author")
        self.assertEqual(len(results), 1)

    def test_search_books_by_year(self):
        """Поиск по году"""
        self.library.add_book("Year Book", "Some Author", 2023)
        results = self.library.search_books(2023)
        self.assertEqual(len(results), 1)

    def test_display_books_empty(self):
        """Отображение книг в пустой библиотеке"""
        self.library.display_books()

    def test_change_status(self):
        """Изменение статуса книги"""
        self.library.add_book("Status Book", "Test Author", 2023)
        book_id = list(self.library.books.keys())[0]
        self.library.change_status(book_id, "выдана")
        self.assertEqual(self.library.books[book_id].status, "выдана")

    def test_change_status_nonexistent_book(self):
        """Изменение статуса несуществующей книги"""
        self.library.add_book("Status Book", "Test Author", 2023)
        book_id = list(self.library.books.keys())[0]

        with self.assertRaises(ValueError) as context:
            self.library.change_status(book_id, "выдана")
            self.library.change_status(999, "в наличии")

        self.assertEqual(str(context.exception), "Ошибка: Книга с таким ID не найдена")
        self.assertEqual(self.library.books[book_id].status, "выдана")

    def test_change_status_invalid_status(self):
        """Изменение статуса с некорректным значением"""
        self.library.add_book("Invalid Status Book", "Test Author", 2023)
        book_id = list(self.library.books.keys())[0]
        with self.assertRaises(ValueError) as context:
            self.library.change_status(book_id, "некорректный статус")

        self.assertEqual(str(context.exception),
                         "Ошибка: Некорректный статус. Доступные статусы: 'в наличии', 'выдана'")
        self.assertEqual(self.library.books[book_id].status, "в наличии")

    def tearDown(self):
        """Очистка после тестов"""
        import os
        if os.path.exists('test_library.json'):
            os.remove('test_library.json')


if __name__ == "__main__":
    unittest.main()
