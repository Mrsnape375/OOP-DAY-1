class Book:
    def __init__(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages
    def describe(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

class Ebook(Book):
    def __init__(self,name,author,pages,file_size):
        super().__init__(name,author,pages)
        self.file_size=file_size
    def describe(self):
        print("----------Ebook Details----------")
        super().describe()
        print(f"Size: {self.file_size} Mb")
        print("-------------------------------")

e=Ebook('Ikigai','Hector Garcia, Francesc Miralles',123,50)
e.describe()