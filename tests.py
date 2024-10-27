import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2


    def test_add_new_book_the_same_name_and_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби, и зомби, и зомби...')

        assert len(collector.get_books_genre()) == 1


    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
            ['Властелин колец', 'Фантастика'],
            ['Приключения Шерлока Холмса', 'Детективы']
        ]
    )
    def test_set_book_genre_positive(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre.get(name) == genre


    def test_set_book_genre_absent_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Кот в сапогах')
        collector.set_book_genre('Кот в сапогах', 'Сказка')

        assert collector.books_genre.get('Кот в сапогах') == ''


    def test_set_book_genre_absent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Кот в сапогах', 'Мультфильмы')

        assert 'Мультфильмы' not in collector.books_genre.values()


    def test_get_book_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.books_genre.get('Гордость и предубеждение и зомби') == 'Ужасы'


    def test_get_books_with_specific_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2


    def test_get_books_with_specific_genre_empty_list(self):
        collector = BooksCollector()

        assert len(collector.get_books_with_specific_genre('Ужасы')) == 0


    def test_get_books_genre_empty_list(self):
        collector = BooksCollector()

        assert collector.get_books_genre() == {}


    def test_get_books_for_children_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мультфильмы')

        assert len(collector.get_books_for_children()) == 2


    def test_add_book_in_favorites_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' in collector.favorites


    def test_add_book_in_favorites_twiсe_negative(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.favorites) == 1


    def test_delete_book_from_favorites_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' not in collector.favorites


    def test_delete_book_from_favorites_empty_books_genre(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert collector.favorites == []#нет ошибки


    def test_get_list_of_favorites_books_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Властелин колец', 'Что делать, если ваш кот хочет вас убить']
