import unittest
from unittest import TestCase


# Класс представляет книгу с идентификатором, названием и автором
class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author


# Класс репозитория книг, имитирующий доступ к данным о книгах
class BookRepository:
    def __init__(self):
        # Простая имитация базы данных книг
        self.books = {
            "1": Book("1", "Book1", "Author1"),
            "2": Book("2", "Book2", "Author2")
        }

    # Метод для поиска книги по идентификатору
    def findById(self, book_id):
        return self.books.get(book_id)

    # Метод для получения списка всех книг
    def findAll(self):
        return list(self.books.values())


# Класс сервиса для работы с книгами
class BookService:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    # Метод для поиска книги по идентификатору с использованием репозитория
    def findBookById(self, book_id):
        return self.book_repository.findById(book_id)

    # Метод для получения списка всех книг с использованием репозитория
    def findAllBooks(self):
        return self.book_repository.findAll()


# Класс для тестирования функциональности BookService
class TestBookService(TestCase):
    # Тест проверяет функцию поиска книги по идентификатору
    def test_find_book_by_id(self):
        book_repository = BookRepository()
        book_service = BookService(book_repository)
        result = book_service.findBookById("1")
        self.assertEqual(result.title, "Book1")

    # Тест проверяет функцию получения списка всех книг
    def test_find_all_books(self):
        book_repository = BookRepository()
        book_service = BookService(book_repository)
        result = book_service.findAllBooks()
        self.assertEqual(len(result), 2)


if __name__ == '__main__':
    # Запуск тестов
    unittest.main()
