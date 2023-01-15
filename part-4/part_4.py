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

def create_book():
    title = input("What is the name of the book you would like to add? ")
    author = input("Who is the author of the book you would like to add? ")
    year = input("What year was the book you would like to add published? ")
    rating = input("What rating would you give the book you would like to add? Rate 1-5. ")
    pages = input("How many pages is the book you would like to add? ")
    
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "page": pages
}
    return book_dictionary
print(create_book)


    
### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

def create_new_list():
    title = input("What is the name of the book you would like to add? ")
    author = input("Who is the author of the book you would like to add? ")
    year = int(input("What year was the book you would like to add published? "))
    rating = float(input("What rating would you give the book you would like to add? Rate 1-5. "))
    pages = int(input("How many pages is the book you would like to add? "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating, 
        "pages": pages
    }

    title = "The Metu Neter"
    return book_dictionary 

# print(type(title))

#I don't think I did this correctly and would like to go over it when possible.  


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

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


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here


def add_new_book ():
    title = input("What is the name of the book you would like to add? ")
    author = input("Who is the author of the book you would like to add ")
    year = input("What year was the book you would like to add published? ")
    rating = input("What rating would you give the book? Rate 1-5. ")
    pages = input("How many pages is the book you would like to add? ")



    def see_all_books(book_dictionary):
        author = book_dictionary['author']
        title = book_dictionary['title']
        year = book_dictionary['year']
        pages = book_dictionary['pages']
        rating = book_dictionary['rating']

   
def find_book_title(book_dictionary):
      author = book_dictionary['author']
      title = book_dictionary['title']
      year = book_dictionary['year']
      pages = book_dictionary['pages']
      rating = book_dictionary['rating']
      
      book_title = f"Here is book {title}. "
      return book_title

print(find_book_title(my_book2)) 

# functions only work when error handling is commented out.


year = 2000
if year < 1800:
    print("This book is historic!")
elif year < 1989:
    print("This book is a classic!")
else:
    print("This book is really pushing the culture of reading forward")

#not understanding how to call the "see all" fuction. Is there a way to makea list of objects a variable?



### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

