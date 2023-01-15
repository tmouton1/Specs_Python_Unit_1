### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["Clarissa Pinkola Estes", "Audre Lorde", "Caroline Shola Arewa", "BKS Iyengar", "Anondea Judith", "Ra Un Nefer Amen", "Toni Morrison"]

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
my_authors.append("Octavia Butler")
# Example: my_authors.append("H.G. Wells")
# print(my_authors)
# Now let's remove an element in the list
print(my_authors)
# Code here
my_authors.remove("Audre Lorde")
# Example: my_authors.remove("H.G. Wells")

print(my_authors)

my_authors.pop()
print(my_authors)

# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
print(my_authors[4])
# Example: my_authors[2]

# Now slice the list.

# Code here
print(my_authors[1:6])

# Example: my_authors[1:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
my_authors_tuple = my_authors = ("Clarissa Pinkola Estes", "Audre Lorde", "Caroline Shola Arewa", "BKS Iyengar", "Anondea Judith", "Ra Un Nefer Amen", "Toni Morrison")
print(my_authors_tuple)
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")



### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
my_authors_set = {"Clarissa Pinkola Estes", "Audre Lorde", "Caroline Shola Arewa", "BKS Iyengar", "Anondea Judith", "Ra Un Nefer Amen", "Toni Morrison"}
print(my_authors_set)

# Add a new author to your set.

# Code here
my_authors_set.add("Deanna Robinson")
print(my_authors_set)
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.
my_authors_set.add("Deanna Robinson")
print(my_authors_set)
# Code here
# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here

# Example:
book_list = ["Metu Neter", "Eastern Mind, Western Body", "Wildseed"]
for book in book_list:
    print(book)
# for book in my_authors:
    # print(book)


# for book in my_authors_tuple:
    # print(book)
book_list_tuple = book_list = ("Metu Neter", "Eastern Mind, Western Body", "Wildseed")
for book in book_list_tuple:
    print(book)


# for book in my_authors_set:
    # print(book)
    book_list_set = {"Metu Neter", "Eastern Mind, Western Body", "Wildseed"}
    for book in book_list_set:
        print(book)

