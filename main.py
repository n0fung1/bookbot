from stats import word_count

def get_book_text(book_path):
    with open(book_path) as book:
        contents = book.read()
        return str(contents)

    
def main():
    num_words = word_count(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document.")
    
main()
