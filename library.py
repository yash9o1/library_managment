class library():
    def __init__(self,books):
        self.books = list(books)
        # self.nbooks = len(books)

    def show(self):
        print(f"The no. of books is {self.nbooks} and the books are:")
        for book in self.books:
            print(book)

    def addBook(self,book):
        self.books.append(book)
        self.nbooks=len(self.books)

    def check(self):
        if self.nbooks==len(self.books):
            print("The code is running successfully")
        else:
            print("The code is not running successfully")

x=library(['Clean code','Refactoring','Coders at Work','Introduction to Algorithms'])
x.addBook('Head First Java')
x.addBook('Learn to code')
x.show()
