import pytest
import main as book


@pytest.fixture(scope='function')
def collector():
    collector = book.BooksCollector()
    return collector

@pytest.fixture
def add_book(collector):
    return collector.add_new_book

@pytest.fixture
def add_genre(collector):
    return collector.set_book_genre
