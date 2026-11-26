#обход книжной полки в обратном порядке
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Book:
    title: str
    author: str


class ForwardBookIterator(Iterator[Book]):

    def __init__(self, books: tuple[Book, ...]):
        self._books = books
        self._index = 0

    def __next__(self) -> Book:
        if self._index >= len(self._books):
            raise StopIteration
        book = self._books[self._index]
        self._index += 1
        return book


class ReverseBookIterator(Iterator[Book]):

    def __init__(self, books: tuple[Book, ...]):
        self._books = books
        self._index = len(books) - 1

    def __next__(self) -> Book:
        if self._index < 0:
            raise StopIteration
        book = self._books[self._index]
        self._index -= 1
        return book


IteratorFactory = Callable[[tuple[Book, ...]], Iterator[Book]]


class BookShelf(Iterable[Book]):

    def __init__(self, iterator_factory: IteratorFactory = ForwardBookIterator):
        self._books: list[Book] = []
        self._iterator_factory = iterator_factory

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def __iter__(self) -> Iterator[Book]:
        return self._iterator_factory(tuple(self._books))

    def custom_iter(self, factory: IteratorFactory) -> Iterator[Book]:
        """Позволяет запустить обход с любым новым итератором без изменения класса."""
        return factory(tuple(self._books))

