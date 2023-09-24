import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize("book_name", [
        'A', 'AB', 'A' * 21, 'A' * 39, 'A' * 40
    ])
    def test_add_new_book_positive(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    @pytest.mark.parametrize("book_name", [
        '', 'A' * 41, 'A' * 48
    ])
    def test_add_new_book_negative(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_set_and_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Genre Book')
        collector.set_book_genre('Genre Book', 'Фантастика')
        assert collector.get_book_genre('Genre Book') == 'Фантастика'
        collector.set_book_genre('Genre Book', 'NA Genre')
        assert collector.get_book_genre('Genre Book') == 'Фантастика'

    @pytest.mark.parametrize("book_name, genre", [
        ('Child Book', 'Комедии'),
        ('Child Book', 'Мультфильмы'),
    ])
    def test_books_for_children_positive(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name in collector.get_books_for_children()

    @pytest.mark.parametrize("book_name, genre", [
        ('Adult Book', 'Ужасы'),
        ('Adult Book', 'Детективы'),
    ])
    def test_books_for_children_negative(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name not in collector.get_books_for_children()

    def test_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Favorite Book')
        collector.add_book_in_favorites('Favorite Book')
        assert 'Favorite Book' in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites('Favorite Book')
        assert 'Favorite Book' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_and_get_list(self):
        collector = BooksCollector()
        collector.add_new_book('Favorite Book')
        collector.add_book_in_favorites('Favorite Book')
        assert 'Favorite Book' in collector.get_list_of_favorites_books(), "Book in books"

    def test_delete_book_from_favorites_and_get_list(self):
        collector = BooksCollector()
        collector.add_new_book('Favorite Book')
        collector.add_book_in_favorites('Favorite Book')
        collector.delete_book_from_favorites('Favorite Book')
        assert 'Favorite Book' not in collector.get_list_of_favorites_books(), "Book not in books"

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
        collector.add_new_book('Favorite Book')
        collector.add_book_in_favorites('Favorite Book')
        assert 'Favorite Book' in collector.get_list_of_favorites_books()