from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_book_more_than_40_symbols(self):
        collector = BooksCollector()
        collector.add_new_book(
            'Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче и о прекрасной царевне Лебеди')
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'book_name, book_genre, expected_result',
        [
            ('Снеговик', 'Детективы', 'Детективы'),
            ('Снеговик', 'Триллер', '')
        ]
    )
    def test_set_book_genre_name_in_books_genre(self, book_name, book_genre, expected_result):
        collector = BooksCollector()
        collector.add_new_book('Снеговик')
        collector.set_book_genre(name=book_name, genre=book_genre)
        assert collector.books_genre.get('Снеговик') == expected_result

    def test_get_book_genre_after_setting_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Задача трёх тел')
        collector.set_book_genre('Задача трёх тел', 'Фантастика')
        assert collector.get_book_genre('Задача трёх тел') == 'Фантастика'

    @pytest.mark.parametrize(
        'book_genre, expected_result',
        [
            ('Детективы', ['Снеговик', 'Подсказчик']),
            ('Фантастика', ['Задача трёх тел']),
            ('Мультфильмы', []),
            ('Детектив', [])
        ]
    )
    def test_get_books_with_specific_genre(self, book_genre, expected_result):
        collector = BooksCollector()
        collector.add_new_book('Снеговик')
        collector.set_book_genre('Снеговик', 'Детективы')
        collector.add_new_book('Задача трёх тел')
        collector.set_book_genre('Задача трёх тел', 'Фантастика')
        collector.add_new_book('Подсказчик')
        collector.set_book_genre('Подсказчик', 'Детективы')
        assert collector.get_books_with_specific_genre(book_genre) == expected_result

    def test_get_books_genre_two_books_in_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Задача трёх тел')
        collector.add_new_book('Снеговик')
        collector.set_book_genre('Снеговик', 'Детективы')
        expected_dict = {'Задача трёх тел': '', 'Снеговик': 'Детективы'}
        assert collector.get_books_genre() == expected_dict

    def test_get_books_for_children_allowed_and_not_allowed_books_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Снеговик')
        collector.set_book_genre('Снеговик', 'Детективы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Винни-Пух и его друзья')
        collector.set_book_genre('Винни-Пух и его друзья', 'Мультфильмы')
        collector.add_new_book('Задача трёх тел')
        collector.set_book_genre('Задача трёх тел', 'Фантастика')
        expected_result = ['Винни-Пух и его друзья', 'Задача трёх тел']
        assert collector.get_books_for_children() == expected_result

    @pytest.mark.parametrize(
        'book_name, expected_result',
        [
            ('Оно', ['Оно']),
            ('Снеговик', [])
        ]
    )
    def test_add_book_in_favorites(self, book_name, expected_result):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites(book_name)
        assert collector.favorites == expected_result

    @pytest.mark.parametrize(
        'book_name, expected_result',
        [
            ('Оно', []),
            ('Снеговик', ['Оно'])
        ]
    )
    def test_delete_book_from_favorites(self, book_name, expected_result):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites(book_name)
        assert collector.favorites == expected_result

    def test_get_list_of_favorites_books_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Винни-Пух и его друзья')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Винни-Пух и его друзья')
        assert collector.get_list_of_favorites_books() == ['Оно', 'Винни-Пух и его друзья']