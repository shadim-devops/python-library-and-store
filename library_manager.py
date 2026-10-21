class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True


class Reader:
    def __init__(self, first_name, last_name, reader_id):
        self.first_name = first_name
        self.last_name = last_name
        self.reader_id = reader_id
        self.borrowed = []


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__books = []
        self.__readers = []

    def add_book(self, book):
        self.__books.append(book)
        print("Book added:", book.title)

    def add_reader(self, reader):
        self.__readers.append(reader)
        print("Reader registered:", reader.first_name, reader.last_name)

    def borrow_book(self, isbn, reader_id):
        for k in self.__books:
            if k.isbn == isbn and k.available:
                for c in self.__readers:
                    if c.reader_id == reader_id:
                        k.available = False
                        c.borrowed.append(k)
                        print("Book borrowed:", k.title)
                        return
        print("Cannot borrow book")

    def return_book(self, isbn, reader_id):
        for c in self.__readers:
            if c.reader_id == reader_id:
                for k in c.borrowed:
                    if k.isbn == isbn:
                        k.available = True
                        c.borrowed.remove(k)
                        print("Book returned:", k.title)
                        return
        print("Book not found for return")

    def search_books(self, query):
        for k in self.__books:
            if query in k.title or query in k.author or query in k.isbn:
                print("Found:", k.title, "-", k.author)

    def show_borrowed_books(self, reader_id):
        for c in self.__readers:
            if c.reader_id == reader_id:
                print("Borrowed books:")
                if len(c.borrowed) == 0:
                    print("No borrowed books")
                for k in c.borrowed:
                    print(k.title)


class CityLibrary(Library):
    def __init__(self, name, address, city):
        super().__init__(name, address)
        self.city = city


library = CityLibrary("City Library", "Main Street 1", "Example City")

k1 = Book("White Fang", "Jack London", "111", 1906)
k2 = Book("The Time Machine", "Herbert Wells", "222", 1895)

library.add_book(k1)
library.add_book(k2)

c1 = Reader("Adam", "Smith", "1")
library.add_reader(c1)

library.borrow_book("111", "1")
library.show_borrowed_books("1")
library.return_book("111", "1")
library.search_books("Wells")
