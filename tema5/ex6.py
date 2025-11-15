class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        return f"{self.title} was not checked out."

    def display_info(self):
        status = "Checked out" if self.checked_out else "Available"
        return f"Title: {self.title}, ID: {self.item_id}, Status: {status}"

class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def display_info(self):
        return f"Book - {super().display_info()}, Author: {self.author}, Pages: {self.pages}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        return f"DVD - {super().display_info()}, Director: {self.director}, Duration: {self.duration} mins"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display_info(self):
        return f"Magazine - {super().display_info()}, Issue No: {self.issue_number}"
    
book = Book("1984", 1, "George Orwell", 328)
dvd = DVD("Inception", 2, "Christopher Nolan", 148)
magazine = Magazine("National Geographic", 3, 202)

print(book.display_info())
print(book.check_out())
print(book.display_info())
print(book.return_item())
print(book.display_info())

print(dvd.display_info())
print(magazine.display_info())