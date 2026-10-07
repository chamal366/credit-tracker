books_IDs = []
titles = []
authors = []
quantitys = []
print("Press 1 to add a new book;")
print("Press 2 to display all available book;")
print("Press 3 to search book;")
print("Press 4 to issue a book ")
print("Press 5 to return a book;")
print("Press 6 to update its quantity")
print("Press 7 to remove a book from the library;")
print("Press 8 to display all books that are currently out of stock;")
print("Press 9 to know total number of books in the library; ")


flag = True
while flag:
    choice = int(input("\n\n\t\t *** Enter any number(1-9)***\t"))
    jhanda = True
    while jhanda:
        if choice == 1:
            id = input("Enter Book ID: ")
            title = input("Enter book title: ")
            author = input("Enter the name of author: ")
            quantity = int(input("Enter how many copies: "))
            bk = input("Do you want to add more books? (y/n)")
            if bk == 'y' or bk == 'Y':
                jhanda = True
            elif bk == 'n' or bk == 'N':
                jhanda = False
            else:
                bs = input(f"You entered {bk} Please Enter either y or n:  ")
                if bs == 'y' or bs == 'Y':
                    jhanda = True
                elif bs == 'n' or bs == 'N':
                    jhanda = False
                else:
                    print("\tYou entered wrong character two times:")
                    print("\tError limit exeeds....")
                    print("\t**You can't add more books now**")
                    jhanda = False

            books_IDs.append(id)
            titles.append(title)
            authors.append(author)
            quantitys.append(quantity)

        elif choice == 2:
            print(f"{'TITLE':<21} {'AUTHOR':<21} {'BOOK ID':<7} {'QUANTITY':<3}")
            for i, j, k, l in zip(titles, authors, books_IDs, quantitys):
                print(f"{i:<21} {j:<21} {k:<7} {l:<3}")
            jhanda = False

        elif choice == 3:
            idt = input("Enter Book ID or Title to search about book: ")
            if idt in books_IDs or idt in titles:
                index = books_IDs.index(idt) or titles.index(idt)
                print(f"Book Title: {titles[index]}")
                print(f"Book Author: {authors[index]}")
                print(f"Book ID: {books_IDs[index]}")
                print(f"Copy Available: {quantitys[index]}")
            else:
                print("Keyword dosen't matched with any Book ID or title")

        
        elif choice == 4:
            issue = input("Enter the title of book which you want to issue:  ")
            if issue in titles:
                idx = titles.index(issue)
                if quantitys[idx] > 0:
                    issued_book = titles[idx].pop()
                    quantitys[idx] -= 1
                    print("\n\t     You have sucessfully issued following book;")
                    print(f"\tBook Title: {titles[idx]}")
                    print(f"\tBook Author: {authors[idx]}")
                    print(f"\tBook ID: {books_IDs[idx]}")
                    print(f"\tCopy Available: {quantitys[idx]}")
                    isu = input("Do yoy want to issue more books? (y/n) :  ")
                    if isu == 'y' or 'Y':
                        jhanda = True
                    elif isu == 'n' or 'N':
                        jhanda = False
                        g