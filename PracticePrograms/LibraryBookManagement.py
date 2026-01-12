# Program: Library Book Manager

print("===== LIBRARY BOOK MANAGER =====")

library = []

def add_book(title, author):
    library.append({"title": title, "author": author})

def search_book(Keyword):
    return[book for book in library if Keyword.lower() in book["title"].lower()]

def remove_book(tittle):
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            return "Book removed"
    return "book not found"

while True:
    print("\n1.Add Book\n2.Search Book\n3.Remove Book\n4.View Library\n5.Exit")
    choice = int(input("choose option:"))

    if choice == 1:
        t = input("Book title:")
        a = input("Author:")
        add_book(t, a)

    elif choice == 2:
        Key = input("search Keyword:")
        result = search_book(Key)
        print("search Result:", result)

    elif choice == 3:
        t = input("Enter title to remove:")
        print(remove_book(t))

    elif choice == 4:
        print("Library", library)

    elif choice == 5:
        break