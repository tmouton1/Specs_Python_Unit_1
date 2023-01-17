print('hello')


### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

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
my_book3= {
    "title": "Beloved",
    "author": "Toni Morisson",
    "year": 1987,
    "rating": 8.5,
    "pages": 324


}
book_list = [my_book, my_book2, my_book3]

# def create_book():
#     title = input("What is the name of the book you would like to add? ")
#     author = input("Who is the author of the book you would like to add? ")
#     year = input("What year was the book you would like to add published? ")
#     rating = input("What rating would you give the book you would like to add? Rate 1-5. ")
#     pages = input("How many pages is the book you would like to add? ")
    
#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "page": pages
# }
#     return book_dictionary
# print(create_book)


    
### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def create_book():
#     title = input("What is the name of the book you would like to add? ")
#     author = input("Who is the author of the book you would like to add? ")
#     year = int(input("What year was the book you would like to add published? "))
#     rating = float(input("What rating would you give the book you would like to add? Rate 1-5. "))
#     pages = int(input("How many pages is the book you would like to add? "))
    
#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "page": pages
#     }
#     return book_dictionary
# print(create_book)


# print(type(title))



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def create_book():
    title = input("What is the name of the book you would like to add? ")
    author = input("Who is the author of the book you would like to add? ")
    
    try: 
        rating = float(input("What rating would you give the book? Rate 1-5. ")) 

    except: 
        rating = float(input("Please type a rating using decimal numbers, i.e. 1.0 or 1.5. "))

    try: 
        year = int(input("What year was the book published? "))

    except: 
        year = int(input("Please enter a number for the pubishing year. "))

    try: 
        pages = int(input("How many pages is the book? "))

    except: 
        pages = int(input("Please enter a number for the amount of book pages. ")) 

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "page": pages
    }
    return book_dictionary
# print(create_book())



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

def see_all_books(book_list):
    for book in book_list:
        title = book["title"]
        book_title = f" {title}."
        print (book_title)
        
def main_menu():
    option = input ("Please choose an option. Choose 1 to add a book to the list. Choose 2 to see all books. Choose 3 to go back to main menu. Choose 4 to exit.")
    
    if option == "1":
        print(input())
        book_list.append(create_book())
    elif option == "2":
        print("Great option! You've chosen to see all books on the list. Here they are: ")
        see_all_books(book_list)
    elif option == "3":
        find_book_title
    elif option == "4":
        print("Thank you for visiting, goodbye")
        
#not sure why none is printing. 

main_menu() 


def find_book_title(book_dictionary):
    author = book_dictionary['author']
    title = book_dictionary['title']
    year = book_dictionary['year']
    pages = book_dictionary['pages']
    rating = book_dictionary['rating']
      
    book_title = f"Here is book, {title}. "
    return book_title
print(find_book_title(my_book))

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

alive = True

while alive: 
    
    option = input("Please choose an option. Choose 1 to add a book to the list. Choose 2 to see all books. Choose 3 to go back to main menu. Choose 4 to exit.")
    if option =="1":
        book_list.append(create_book())
    elif option == "2":    
        see_all_books(book_list)
    elif option == "3":
        print(main_menu())
    elif option == "4":
        print("Thank you for visiting, goodbye")
    

      #would like help with while loop. Struggling to figure out how to exit loop properly.