print("hello git from my side")

for i in range(10):
    print(i)

class Books:
    def __init__(self, book_name):
        self.book_name = book_name

    def __repr__(self):
        return self.book_name
    

def name():
    book = Books("Gita")
    print(book)
