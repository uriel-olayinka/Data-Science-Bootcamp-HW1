books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "rating": 4.2
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "rating": 4.5
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "rating": 4.8
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.7
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "rating": 4.9
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-age",
        "rating": 4.1
    }
]


def check_rating(book):
    for bk in books:
        if bk["title"] == book:
            if bk["rating"] > 4.5:
                #return True
                return "high"
            #return False
            elif 4.0 < bk["rating"] <= 4.5:
                return "medium"
            else:
                return "low"


def average_rating_by_genre(books, genre):
    is_genre_in_list = False
    avg_rating = 0
    num_nums = 0
    for book in books:
        if book["genre"] == genre:
            is_genre_in_list = True
            avg_rating += book["rating"]
            num_nums += 1
    if is_genre_in_list:
        avg_rating = avg_rating / num_nums
        return avg_rating
    return "There are no " + genre + " books in the list"


def books_by_author(books, author):
    is_author_in_list = False
    author_booklist = []
    for book in books:
        if book["author"] == author:
            is_author_in_list = True
            author_booklist.append(book["title"])
    if is_author_in_list:
        return author_booklist
    else:
        return "There are no books by " + author + " in the list"


def main():
    bk1 = "Harry Potter and the Sorcerer's Stone"
    bk2 = "The Catcher in the Rye"
    print(check_rating(bk1))
    print(check_rating(bk2))

    print(average_rating_by_genre(books, "Fantasy"))

    author1 = "J.K. Rowling"
    author2 = "William Shakespeare"
    print(books_by_author(books, author1))
    print(books_by_author(books, author2))


main()
