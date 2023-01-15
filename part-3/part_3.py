my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book2 = {
    "title": "Celestine Prophecy",
    "author": "James Redfield",
    "year": 1999,
    "rating": 8.5,
    "pages": 368
}




# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

print("hello")


def book_parser(book_dictionary):

    author = book_dictionary['author']
    title = book_dictionary['title']
    year = book_dictionary['year']
    pages = book_dictionary['pages']
    rating = book_dictionary['rating']


    book_string = f" The book {title} was written by {author} in {year}. It is {pages} and has a rating of {rating}."

    return book_string
    

print(book_parser(my_book2))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def call_author(book_dictionary):
    author = book_dictionary['author']
    book_author = f"{author}"
    return book_author

print(call_author(my_book))


def call_rating(book_dictionary):
    rating = book_dictionary['rating']
    book_rating = f"{rating}"
    return book_rating

print(call_rating(my_book))

def call_title(book_dictionary):
    title = book_dictionary['title']
    book_title = f"{title}"
    return book_title

print(call_title(my_book))    




# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def call_main(book_dictionary):

    author = book_dictionary['author']
    title = book_dictionary['title']
    year = book_dictionary['year']
    pages = book_dictionary['pages']
    rating = book_dictionary['rating']

    book_main = f"The book {title} is written by {author}. "
    return book_main

print(call_main(my_book))


def call_published(book_dictionary):
    author = book_dictionary['author']
    title = book_dictionary['title']
    year = book_dictionary['year']
    pages = book_dictionary['pages']
    rating = book_dictionary['rating']

    book_published = f"The book {title} was published in {year}."
    return book_published
print(call_published(my_book))


def call_pages(book_dictionary):
    author = book_dictionary['author']
    title = book_dictionary['title']
    year = book_dictionary['year']
    pages = book_dictionary['pages']
    rating = book_dictionary['rating']

    book_pages = f"The book {title} is {pages} pages long."
    return book_pages
print(call_pages(my_book2))
