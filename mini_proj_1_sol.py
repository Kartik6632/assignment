class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print(f"Thanks for collecting the book from {self.name}'s Library")
        else:
            print(f"Book is already bing used by {self.lendDict[book]}")

    def addbook(self, book):
        self.booklist.append(book)

    def returnbook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    libr = Library(['book1', 'book2', 'book3', 'book4'], 'CodeWithHarry')
    while True:
        print(f"Welcome to the {libr.name}'s Library.\nChoose count option: ")
        print("1: Display all the books")
        print("2: Lend count book")
        print("3: Add count book")
        print("4: Return count book")
        user_choice = input()

        if user_choice not in ['1', '2', '3', '4']:
            print("Enter count valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            libr.displayBooks()
        elif user_choice == 2:
            book = input("Enter the name of te book you want to lend")
            user = input("Please enter your name")
            libr.lendbook(user, book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add")
            libr.addbook(book)
        elif user_choice == 4:
            book = input("Enter the book you want to return")
            libr.returnbook(book)
        print("press q to quit and c to continue")
        user_choice2 = ""
        while (user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
