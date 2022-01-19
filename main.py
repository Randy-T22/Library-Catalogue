def information_print() -> None:
  print("Welcome to the Librarian's Catalogue! You may choose to [add] or [remove] books from the catalogue. You may also [check] the information of books placed within the Catalogue, as well as search for a specific book by [title], [author], or [genre]. In case of mistaken information being placed within a book, you may [update]. Whenever you are finished, you may [quit] the program.")


def invalid_input_title(name_input: str) -> str:
    with open("books_list.txt") as file:
      for line in file:
        if name_input in line:
          return line
      return "False"


def invalid_input_author(author_input: str) -> str:
    with open("books_list.txt") as file:
      for line in file:
        if author_input in line:
          return line
      return "False"
      

def invalid_input_genre(genre_input: str) -> str:
  with open("books_list.txt") as file:
    for line in file:
      if genre_input in line:
        return line
    return "False"


def add_book() -> None:
  book_title = input("Title: ")
  book_author = input("Author: ")
  book_genre = input("Genre: ")
  publication_year = input("Year of Publication: ")
  with open("books_list.txt", "a") as books:
    books.write(f"{book_title} by {book_author} ({book_genre}), written in {publication_year}\n")


def remove_book() -> None:
  name_input = input("Name of Book: ")
  if invalid_input_title(name_input) == "False":
    print("Book cannot be found")
  else:
    book = open("books_list.txt")
    lines = book.readlines()
    book.close()
    with open("books_list.txt", "w") as file:
      for line in lines:
        if not name_input in line.strip("\n"):
          file.write(line)


def check_all_books() -> None:
  with open("books_list.txt") as file:
    for line in file:
      print(line.strip("\n"))


def check_title() -> None:
  name_input = input("Name of Book: ")
  if invalid_input_title(name_input) == "False":
    print("Book cannot be found")
  else:
    with open("books_list.txt") as file:
      for line in file:
        if name_input in line:
          print(line.strip("\n"))


def check_author() -> None:
  author_input = input("Name of Author: ")
  if invalid_input_author(author_input) == "False":
    print("Book cannot be found")
  else:
    with open("books_list.txt") as file:
      for line in file:
        if author_input in line:
          print(line.strip("\n"))


def check_genre() -> None:
  genre_input = input("Genre: ")
  if invalid_input_genre(genre_input) == "False":
    print("Book cannot be found")
  else:
    with open("books_list.txt") as file:
      for line in file:
        if genre_input in line:
          print(line.strip("\n"))


def update_book() -> None:
      name_input = input("Name of Book: ")
      if invalid_input_title(name_input) == "False":
        print("Book not found")
      with open("books_list.txt") as file:
        for line in file:
          if name_input in line:
            book_author = input("Author: ")
            book_genre = input("Genre: ")
            publication_year = input("Year of Publication: ")
            book = open("books_list.txt")
            lines = book.readlines()
            book.close()
            with open("books_list.txt", "w") as file:
              for line in lines:
                if not name_input in line.strip("\n"):
                    file.write(line)
              file.write(f"{name_input} by {book_author} ({book_genre}), written in {publication_year}\n")
              break

def main() -> None:
  information_print()
  while True:
    print("\nAvailable commands are:\n[add], [remove] [check], [title], [author], [genre], [update], [quit]")
    user_input = input("\n> ")
    if user_input == "add":
      add_book()
    elif user_input == "remove":
      remove_book()
    elif user_input == "check":
      check_all_books()
    elif user_input == "title":
      check_title()
    elif user_input == "author":
      check_author()
    elif user_input == "genre":
      check_genre()
    elif user_input == "update":
      update_book()
    elif user_input == "quit":
      break
    else:
      print("Please choose a valid option.")
    

if __name__ == '__main__':
  main()
