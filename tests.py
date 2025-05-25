import pytest

from data import BOOK, GENRE


class TestBooksCollector:

    def test_add_book(self, collector, add_book):
        add_book(BOOK)
        assert collector.books_genre.get(BOOK) is not None

    def test_add_book_long_name(self, collector, add_book):
        name = 'A' * 41
        add_book(name)
        assert name not in collector.books_genre

    def test_add_book_duplicated_name(self, collector, add_book):
        add_book(BOOK)
        add_book(BOOK)
        assert list(collector.books_genre.keys()).count(BOOK) == 1

    def test_set_book_genre(self, collector, add_book, add_genre):
        add_book(BOOK)
        add_genre(BOOK, GENRE)
        assert collector.books_genre.get(BOOK) is GENRE

    def test_get_book_genre(self, collector, add_book):
        add_book(BOOK)
        assert collector.get_book_genre(BOOK) == ''

    @pytest.mark.parametrize("book_name, genre", [
        (BOOK, GENRE),
        ("Шерлок Хомс", "Детективы"),
    ])
    def test_get_books_with_specific_genre(self, collector, add_book, add_genre, book_name, genre):
        add_book(book_name)
        add_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    @pytest.mark.parametrize("book_name, genre", [
        (BOOK, GENRE),
        ("Шерлок Хомс", "Детективы"),
    ])
    def test_get_books_for_children(self, collector, add_book, add_genre, book_name, genre):
        add_book(book_name)
        add_genre(book_name, genre)
        assert collector.get_books_for_children() == [BOOK]

    def test_add_book_in_favorites(self, collector, add_book):
        add_book(BOOK)
        collector.add_book_in_favorites(BOOK)
        assert BOOK in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector, add_book):
        add_book(BOOK)
        collector.add_book_in_favorites(BOOK)
        collector.delete_book_from_favorites(BOOK)
        assert BOOK not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []
