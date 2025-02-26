from stats import word_count, char_count, sort_on, char_sort

def get_book_text(book_path):
    with open(book_path) as book:
        contents = book.read()
        return str(contents)

    
def main():
    BOOKBOT_HEADING = "============ BOOKBOT ============"
    WORD_COUNT_HEADING = "----------- Word Count ----------"
    CHARACTER_COUNT_HEADING = "--------- Character Count -------"
    BOOKBOT_END = "============= END ==============="

    num_words = word_count(get_book_text("./books/frankenstein.txt"))
    frank_char_count = char_sort(char_count(get_book_text("./books/frankenstein.txt")))

    
    print(BOOKBOT_HEADING)
    print("Analyzing book found at books/frankenstein.txt...")
    print(WORD_COUNT_HEADING)
    print(f"Found {num_words} total words")
    print(CHARACTER_COUNT_HEADING)
    
    for i in range(0, len(frank_char_count)):
        for k in frank_char_count[i]:
            if k.isalpha():
                print(f"{k}: {frank_char_count[i][k]}")
    print(BOOKBOT_END)
main()
