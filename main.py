def get_book_text(book_path):
    with open(book_path) as book:
        contents = book.read()
        return str(contents)

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()
