class Library:
    def __init__(self):
        self.books = []  # Список книг в библиотеке

    def add_book(self, book_title):
        """Добавляет книгу в список."""
        self.books.append(book_title)
        print(f'Книга "{book_title}" добавлена в библиотеку.')

    def remove_book(self, book_title):
        """Удаляет книгу из списка."""
        if book_title in self.books:
            self.books.remove(book_title)
            print(f'Книга "{book_title}" удалена из библиотеки.')
        else:
            print(f'Книга "{book_title}" не найдена в библиотеке.')

    def find_book(self, book_title):
        """Ищет книгу по названию."""
        if book_title in self.books:
            print(f'Книга "{book_title}" найдена в библиотеке.')
        else:
            print(f'Книга "{book_title}" отсутствует в библиотеке.')

    def show_books(self):
        """Выводит список всех книг в библиотеке."""
        if not self.books:
            print("В библиотеке пока нет книг.")
        else:
            print("Список книг в библиотеке:")
            for book in self.books:
                print(f"- {book}")

if __name__ == "__main__":
    my_library = Library()

    my_library.add_book("Война и мир")
    my_library.add_book("Преступление и наказание")
    my_library.add_book("1984")

    my_library.show_books()

    my_library.find_book("1984")
    my_library.find_book("Мастер и Маргарита")

    my_library.remove_book("Преступление и наказание")
    my_library.remove_book("Анна Каренина")

    my_library.show_books()