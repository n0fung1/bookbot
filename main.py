def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def open_file(file_to_open):
    with open(file_to_open) as f:
        return f.read()

def count_letters(file_contents):
    words = file_contents.split()
    letter_count = {}
    for word in words:
        #
    print(letter_count)


def main():
    file_to_open = "books/frankenstein.txt"
    file_contents = open_file(file_to_open)
    word_count = count_words(file_contents)
    print(f"{word_count} words in {file_to_open}")
    count_letters(file_contents)



main()