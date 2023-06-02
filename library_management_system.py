class Book:
    def __init__(self, book_id, title, author, genre, borrowed):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = False


class Library:

    def __init__(self, name):
        self.name = name
        self.book_dict = {}

    def add_book(self, obj):
        self.book_dict.update({obj.book_id: obj})

    def get_all_books(self):
        """ get all books """
        count = len([book for book in self.book_dict.values()])
        print("Total Books: ", count)

    def get_books_by_author(self, author_name):
        """ get books by author """
        print("Books by Author: ")
        author_books = [book.title for book in self.book_dict.values() if book.author == author_name]
        print(author_books)

    def get_books_by_genre(self, genre_name):
        """ get books by genre """
        print("Books by Genre: ")
        genre_books = [book.title for book in self.book_dict.values() if book.genre == genre_name]
        print(genre_books)

    def get_books_by_id(self, by_id):
        """ get books by ID """
        print("Books by Book ID: ")
        book_list = [book.title for book in self.book_dict.values() if book.book_id == by_id]
        print(book_list)

    def borrow_book(self, book_id):
        """ get books by ID """
        for book in self.book_dict.values():
            if book.book_id == book_id:
                book.borrowed = True

    def get_borrowed_books(self):
        """ get borrowed books  """
        borrowed_count = sum(1 for book in self.book_dict.values() if book.borrowed)
        print("Total number of borrowed books: ", borrowed_count)

    def get_available_books(self):
        """ get available books  """
        available_books = sum(1 for book in self.book_dict.values() if not book.borrowed)
        print("Total number of available books: ", available_books)


if __name__ == "__main__":
    print("------------ Welcome to Library Management System ------------")

    obj_lib = Library(" Library ")
    opt = True
    while True:
        try:
            select_num = int(input(" 1. Add book to library \n 2. Get Books  \n 3. Get Borrowed Books \n "
                                   "4. Get Available Books \n 5. Books Borrowed \n "
                                   "6. Get book by author \n 7. Get book by genre \n "
                                   "8. Get book by Book Id \n9. Exit \n "))
            match select_num:

                # add Books
                case 1:
                    book_id = input("Enter Book ID : ")
                    title = input("Enter Title : ")
                    author = input("Enter Author : ")
                    genre = input("Enter genre : ")
                    borrowed = int(input("Enter borrowed No. : "))

                    obj = Book(book_id, title, author, genre, borrowed)
                    obj_lib.add_book(obj)
                    print("*************************** Book Added to Library ***************************")

                # display all Books
                case 2:
                    # book_id = input("Enter Book ID : ")
                    obj_lib.get_all_books()

                    print("*************************** Book Details Displayed ***************************")

                # number of books borrowed
                case 3:
                    obj_lib.get_borrowed_books()

                # number of available books
                case 4:
                    obj_lib.get_available_books()

                # book borrowed
                case 5:
                    book_id = input("Enter Book ID : ")
                    obj_lib.borrow_book(book_id)
                    print("----Book Borrowed Successfully-----")

                # Book by author
                case 6:
                    author_name = input("Enter author name : ")
                    obj_lib.get_books_by_author(author_name)

                # Books bye genre
                case 7:
                    genre_name = input("Enter genre name : ")
                    obj_lib.get_books_by_genre(genre_name)

                # books by id
                case 8:
                    by_id = input("Enter Book ID : ")
                    obj_lib.get_books_by_id(by_id)

                # exit
                case 9:
                    user_input = input("Enter y to stop:  ")
                    if user_input == "y":
                        break
                    opt = False
        except Exception as e:
            print(e)

    # def update_details(self, book_id):
    #     search_book = self.book_dict.get(book_id)
    #     if search_book:
    #         search_book.title = input("Enter Title : ")
    #         search_book.author = input("Enter Author : ")
    #         search_book.genre = input("Enter Genre : ")
    #         search_book.borrowed = int(input("Enter Borrowed No. : "))
    #         # self.book_dict.update(name)
    #         print("Details updated")
    #
    # def delete_details(self, book_id):
    #     search_book = self.book_dict.get(book_id)
    #     if search_book:
    #         self.book_dict.pop(book_id)
    #     else:
    #         raise "Please enter a valid Book ID"
