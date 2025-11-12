#Create a class Publisher (name). Derive a class Book (title, author) from Publisher. Derive a class Python (price, no_of_pages) from Book.
# Write a program that displays information about a Python book. Use base class constructor invocation and method overriding.
class Publisher:
    def __init__(self,name):
        self.name=name

    def display(self):
        print( f"Publisher: {self.name}")

class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author

    def display(self):
        super().display()
        print( f"Title : {self.title}\nAuthor : {self.author}")

class Python(Book):
    def __init__(self,name,title,author,price,no_of_pages):
        super().__init__(name,title,author)
        self.price=price
        self.no_of_pages=no_of_pages

    def display(self):
        super().display()
        print(f"Price : {self.price}\nPages : {self.no_of_pages}")



book=Python('Shroff Publishers','Python for Everybody','Charles Severance',75,368)
book.display()

