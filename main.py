# python main.py

from models.library import Library


def main_logic():
    """Главная функция для взаимодействия с пользователем"""
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)

        elif choice == '2':
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                library.remove_book(book_id)
            except ValueError:
                print("Ошибка: Введите корректный числовой ID")

        elif choice == '3':
            query = input("Введите название, автора или год для поиска: ")
            results = library.search_books(query)
            if results:
                for book in results:
                    print(book)
            else:
                print("Книги не найдены.")

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            try:
                book_id = int(input("Введите ID книги для изменения статуса: "))
                new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
                library.change_status(book_id, new_status)
            except ValueError:
                print("Ошибка: Введите корректный числовой ID")

        elif choice == '6':
            print("Выход из программы")
            break

        else:
            print("Ошибка: Некорректный выбор. Попробуйте снова")


if __name__ == '__main__':
    main_logic()
