### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def create_book(book_list):
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


    with open("library.txt", "a") as file:
        file.write("title, author, year, rating, pages/n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def view_all_books(book_list):
    print("Here is a list of our full book catalog.")
    with open("library.txt", "r") as f:
       file = f.readlines()

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

