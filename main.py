def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def open_file(file_to_open):
    with open(file_to_open) as f:
        return f.read()

def count_letters(file_contents):
    words = file_contents.split()
    letter_count = {}
    lower_words = [] 
    for word in words:
        lower_words.append(word.lower())
    for word in lower_words:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] = letter_count[letter] + 1
            else:
                letter_count[letter] = 1
    return letter_count

def convert_to_list_dict(dictionary):
    list_of_dicts = []
    for k in dictionary:
        if k.isalpha():
            list_of_dicts.append({"character":k, "num":dictionary[k]})
    return list_of_dicts

def sort_on(dict):
    return dict["num"]

def main():
    file_to_open = "books/frankenstein.txt"
    file_contents = open_file(file_to_open)
    word_count = count_words(file_contents)
    character_list_dict = count_letters(file_contents)
    print(f"--- Begin report of {file_to_open} ---")
    print(f"{word_count} words in the document\n")
    final_list = convert_to_list_dict(character_list_dict)
    final_list.sort(reverse=True, key=sort_on)
    for d in final_list:
        print(f"The {d["character"]} character was found {d["num"]} times.")
    print("\n--- End report ---")
    #print(character_list_dict['p'])
main()
