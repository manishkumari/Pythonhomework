class Publication:
    def _init_(self, name):
        self.name = name

class Book(Publication):
    def _init_(self, name, author, page_count):
        super()._init_(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")

class Magazine(Publication):
    def _init_(self, name, chief_editor):
        super()._init_(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")


magazine = Magazine("Donald Duck", "Aki Hyyppa")
book = Book("Compartment No. 6", "Rosa Liksom", 192)

magazine.print_information()
print("---------------------------------")
book.print_information()
