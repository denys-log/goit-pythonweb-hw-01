import logging
from abc import ABC, abstractmethod
from typing import List

# Налаштування логування
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Принцип єдиної відповідальності (SRP)
class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title: str = title
        self.author: str = author
        self.year: str = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Принцип розділення інтерфейсів (ISP)
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


# Принцип підстановки Лісков (LSP) та відкритості/закритості (OCP)
class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def show_books(self) -> None:
        if not self.books:
            logger.info("No books in the library.")
        for book in self.books:
            logger.info(book)


# Принцип інверсії залежностей (DIP)
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logger.info(f'Book "{title}" added successfully!')

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        logger.info(f'Book "{title}" removed successfully!')

    def show_books(self) -> None:
        self.library.show_books()


# Основний цикл програми
def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logger.info("Exiting the program. Goodbye!")
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
