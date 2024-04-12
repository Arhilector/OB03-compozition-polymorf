#Создайте класс Author и класс Book.
# Класс Book должен использовать композицию
# для включения автора в качестве объекта.


#агрегация

class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info_about_book(self):
        print(f"""Книга {self.title} написана {self.author.name} {self.author.nationality}""")


author = Author("лев Толстой", "русский")
book = Book("Война и мир", author)

print(author.name)
book.get_info_about_book()




    

    



