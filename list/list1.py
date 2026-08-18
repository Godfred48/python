books = []

while True :
    novel = input("Enter a book you have read: ")
    books.append(novel)

    if novel.lower() == "end":
        break
for book in books:
    print(book)