# Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(title):
    """Display you favorite book"""
    print(f"My favorite book is {title}")

titulo = input("Enter the title of you favorite book: ")

favorite_book(titulo)