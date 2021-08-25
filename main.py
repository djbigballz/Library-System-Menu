###############################
# Cameron Denny               #
# Library System Application  #
# 28/04/2021                  #
###############################


# Menu System
class Menu():
    def __init__(self):
        self.data_initialize()
        print("********* Welcome To The Library System Menu *********")
        while True:
            self.choice = input(""" 
            1: Display books in stock
            2: Display DVD's in stock
            3: Display all items in stock
            4: Add new items to stock
            5: Search for specific item in stock
            6: Delete item from stock
            7: Update item in stock
            8: Quit application
            Please enter your choice: """)

            if self.choice == "1":
                self.view_books()
            elif self.choice == "2":
                self.view_films()
            elif self.choice == "3":
                self.view_all_items()
            elif self.choice == "4":
                self.add_items()
            elif self.choice == "5":
                self.search_item()
            elif self.choice == "6":
                self.delete_item()
            elif self.choice == "7":
                self.update_item()
            elif self.choice == "8":
                break
            else:
                print("You must only select 1,2,3,4,5,6,7,8.")
                print("Please try again")

    # Function to
    def data_initialize(self):
        self.film_dict = {}
        self.book_dict = {}
        # Film Initializer
        film_file = open("films.txt", "r")
        films = film_file.readlines()
        for film in films:
            film = film.replace('\n', '')
            film_data = film.split(',')
            self.film_dict[film_data[0]] = film_data[1:]
        film_file.close()
        # Books intializer
        book_file = open("books.txt", "r")
        books = book_file.readlines()
        for book in books:
            book = book.replace('\n', '')
            book_data = book.split(',')
            self.book_dict[book_data[0]] = book_data[1:]
        book_file.close()

    def view_books(self):
        print('\n******************** All Books in Stock ********************')
        print(str('NO. Books Name || Author firstname, Author secondname || Reference No'))
        num = 0
        for book in self.book_dict.keys():
            num += 1
            print(
                f"{num}. {book} || {self.book_dict[book][0]},{self.book_dict[book][1]} || {self.book_dict[book][2]}"
            )

    def view_films(self):
        print('\n******************** All Films in Stock ********************')
        print("NO. Film Name || Release || Status || Ranking || Genre")
        for film in self.film_dict.keys():
            print(
                f'{film}. {self.film_dict[film][0]} || {self.film_dict[film][1]} || {self.film_dict[film][2]} || {self.film_dict[film][3]} || {self.film_dict[film][4]}'
            )

    def view_all_items(self):
        self.view_books()
        self.view_films()

    def add_items(self):
        while True:
            stock_type = input('''
            Currently we have both books and films in stock, select one of them:
            1: To add a film
            2: To add a book
            3: Back to Main Menu: ''')
            if stock_type == '1':
                while True:
                    new_film = input('''
                    Please enter a new film such as:
                    Film name,Year of release,Status,Ranking,Genre
                    (such as: Ghostbusters,2016,PG,116,Comedy): ''')
                    new_film_data = new_film.split(',')
                    if (new_film_data in self.film_dict.values()):
                        print('''Please enter new and appropriate data''')
                        choise = input(
                            '''Do you want to enter another? (Y/N): ''')
                        if choise.lower() == 'y':
                            continue
                        else:
                            break
                    else:
                        no_of_film = '0' + str(len(self.film_dict) + 1)
                        film_file = open('films.txt', 'a')
                        film_file.write(f"\n{no_of_film},{new_film}")
                        film_file.close()
                        print(
                            '----------------------------------------------------'
                        )
                        print('Your given entry was successfully added')
                        print(
                            '----------------------------------------------------'
                        )
                        break

            if stock_type == '2':
                while True:
                    new_book_input = input('''
                    Please enter a new book such as:
                    Book Name, Author 1 Name, Author 2 Name, Reference Number: 
                    (such as: Send Me No Flowers,Gaylor,Crosse,171938297-2) '''
                                           )
                    new_book = new_book_input.split(',')
                    if new_book[0] in self.book_dict.keys():
                        print('''Please enter new and appropriate data''')
                        choise = input(
                            '''Do you want to enter another? (Y/N): ''')
                        if choise.lower() == 'y':
                            pass
                        else:
                            break
                    else:
                        book_file = open('books.txt', 'a')
                        book_file.write(f"{new_book_input}\n")
                        book_file.close()
                        print(
                            '----------------------------------------------------'
                        )
                        print('Your given entry was successfully added')
                        print(
                            '----------------------------------------------------'
                        )
                        break
            if stock_type == '3':
                break
            else:
                print('Please input an appropriate number....')
        return

    def search_item(self):
        while True:
            search_type = input('''
            Currently we have both books and films in stock, select one of them:
            1: For Films
            2: For Books
            3: Go back To main Menu ''')
            if search_type == '1':
                entered_film = input('''
                Enter the film name you are looking for: ''')
                film_file = open('films.txt', 'r').readlines()
                for film in film_file:
                    film_data = film.split(',')
                    if (film_data[1] == entered_film):
                        print(
                            '----------------------------------------------------'
                        )
                        print(
                            "NO || Film Name || Release || Status || Ranking || Type"
                        )
                        try:
                            print(
                                f'{film_data[0]} || {film_data[1]} || {film_data[2]} || {film_data[3]} || {film_data[4]} || {film_data[5]}'
                            )
                        except:
                            print(film)
                        print(
                            '----------------------------------------------------'
                        )
                        break
                else:
                    print('We do not have this film in our stock')
                choise = input(
                    'Do you want to search for something else? (Y/N): ')
                if choise.lower() == 'y':
                    continue
                else:
                    break
            if search_type == '2':
                entered_book = input('''
                Enter The book name you are looking for: ''')
                book_file = open('books.txt', 'r').readlines()
                for book in book_file:
                    book_data = book.split(',')
                    if (book_data[0] == entered_book):
                        print(
                            '----------------------------------------------------'
                        )
                        print(
                            'Books Name || Writer 1,Writer 2 || Reference No')
                        try:
                            print(
                                f'{book_data[0]} || {book_data[1]} || {book_data[2]} || {book_data[3]}'
                            )
                        except:
                            print(book)
                        print(
                            '----------------------------------------------------'
                        )
                        break
                else:
                    print('We dont have this book in our stock')
                choise = input('Do you want to search for more? (Y/N): ')
                if choise.lower() == 'y':
                    continue
                else:
                    break
            if search_type == '3':
                break

        return

    def delete_item(self):
        while True:
            search_type = input('''
            Currently we have both books and films in stock, select one of them:
            1: For Films
            2: For Books
            3: Go back to main menu ''')
            if search_type == '1':
                entered_film = input('''
                Enter The film name you want to delete: ''')
                film_file = open('films.txt', 'w')
                for No, film in self.film_dict.items():
                    if film[0] == entered_film:
                        pass
                    else:
                        film_file.write(
                            f'{No},{film[0]},{film[1]},{film[2]},{film[3]},{film[4]}\n'
                        )
                print('----------------------------------------------------')
                print('Your given entry has been successfully deleted')
                print('----------------------------------------------------')
                film_file.close()
            if search_type == '2':
                entered_book = input('''
                Enter the book name you want to delete: ''')
                book_file = open('books.txt', 'w')
                for book in self.book_dict.keys():
                    if book == entered_book:
                        pass
                    else:
                        book_file.write(
                            f'{book},{self.book_dict[book][0]},{self.book_dict[book][1]},{self.book_dict[book][2]}\n'
                        )
                print('----------------------------------------------------')
                print('Your given entry has been successfully deleted')
                print('----------------------------------------------------')
                book_file.close()
            if search_type == '3':
                break
            return

    def update_item(self):
        while True:
            search_type = input('''
            Currently we have both books and films in stock, select one of them:
            1: For Films
            2: For Books
            3: Go Back To main Menu ''')
            if search_type == '1':
                entered_film = input('''
                Enter The film name you want to update: ''')
                film_file = open('films.txt', 'w')
                for No, film in self.film_dict.items():
                    if film[0] == entered_film:
                        update_film = input('''
                        Please enter updated film such as:
                        Film name,Year of release,Status,Ranking,Genre
                        (such as: Ghostbusters,2016,PG,116,Comedy): ''')
                        update_film = update_film.split(',')
                        try:
                            film_file.write(
                                f'{No},{film[0]},{update_film[1]},{update_film[2]},{update_film[3]},{update_film[4]}\n'
                            )
                        except:
                            print('Please enter appropriate data...')
                            film_file.write(
                                f'{No},{film[0]},{film[1]},{film[2]},{film[3]},{film[4]}\n'
                            )

                    else:
                        film_file.write(
                            f'{No},{film[0]},{film[1]},{film[2]},{film[3]},{film[4]}\n'
                        )
                print('----------------------------------------------------')
                print('Your given entry has been successfully updated')
                print('----------------------------------------------------')
                film_file.close()
            if search_type == '2':
                entered_book = input('''
                Enter the book name you want to update: ''')
                book_file = open('books.txt', 'w')
                for book in self.book_dict.keys():
                    if book == entered_book:
                        update_book_input = input('''
                        Please enter new book, such as::
                        Book Name, Author 1st Name, Auther 2nd Name, Reference Number: 
                        (such as: Send Me No Flowers,Gaylor,Crosse,171938297-2) '''
                                                  )
                        update_book = update_book_input.split(',')
                        try:
                            book_file.write(
                                f'{book},{update_book[0]},{update_book[1]},{update_book[2]}\n'
                            )
                        except:
                            print('Please Enter an approriate Data...')
                            book_file.write(
                                f'{book},{self.book_dict[book][0]},{self.book_dict[book][1]},{self.book_dict[book][2]}\n'
                            )
                    else:
                        book_file.write(
                            f'{book},{self.book_dict[book][0]},{self.book_dict[book][1]},{self.book_dict[book][2]}\n'
                        )
                print('----------------------------------------------------')
                print('Your given entry has been successfully updated')
                print('----------------------------------------------------')
                book_file.close()
            if search_type == '3':
                break
            return

m = Menu()
