class Book:
    total_books =0




    def __init__(self,headline,writer) -> None:
        self.headline = headline
        self.writer = writer
        Book.total_books+=1


    @classmethod
    def get_books(self):
        return self.total_books
   


book1 = Book("Society","Mansur")
book2 = Book("Culture","Rahim")


total = Book.get_books()
print(total)