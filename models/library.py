from .book import Book


class Library:
    def __init__(self):
        self.books = {}
        self.next_id = 1

    def add_book(self, title, author, year):
        book = Book(self.next_id, title, author, year)
        self.books[self.next_id] = book
        self.next_id += 1
        print(f"Книга '{title}' добавлена с ID {book.book_id}")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Книга с ID {book_id} удалена")
        else:
            print("Книга с таким ID не найдена")

    def search_books(self, query):
        results = [book for book in self.books.values() if
                   query.lower() in book.title.lower() or
                   query.lower() in book.author.lower() or
                   str(book.year) == str(query)]

        return results

    def display_books(self):
        if not self.books:
            print("Библиотека пуста")
        else:
            for book in self.books.values():
                print(book)

    def change_status(self, book_id, new_status):
        if book_id in self.books and new_status in ["в наличии", "выдана"]:
            self.books[book_id].status = new_status
            print(f"Статус книги с ID {book_id} изменен на '{new_status}'")
        else:
            print("Некорректный ID или статус")

