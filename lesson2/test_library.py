from book import Book
from library import Library
import pytest

lib = Library()
b = Book("kkk", "lll")
lib.add_user("Miri")


def test_add_book():
    length = len(lib.books)
    lib.add_book(b)
    assert length + 1 == len(lib.books)


def test_add_user():
    length = len(lib.users)
    lib.add_user("tzipi")
    assert length + 1 == len(lib.users)


def test_check_out_book():
    length = len(lib.checked_out_books)
    lib.check_out_book("tzipi", b)
    assert length + 1 == len(lib.checked_out_books)


def test_return_book():
    assert lib.return_book("Miri", b)


def test_search_book():
    assert b in lib.search_books("kkk")


def test_no_exists_book():
    lib.check_out_book("Miri", "ooo")


def test_special_notes():
    lib.add_book(Book("123", "!@"))
