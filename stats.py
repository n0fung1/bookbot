def word_count(text):
    text_list = text.split()
    return len(text_list)

def char_count(text):
    char_count_dict = {}
    for char in text:
        if char.lower() in char_count_dict:
            char_count_dict[char.lower()] += 1
        else:
            char_count_dict[char.lower()] = 1
    return char_count_dict

def sort_on(dict):
    for k in dict:
        return dict[k]

def char_sort(char_dict):
    characters = []

    for k in char_dict:
        new_dict = {k: char_dict[k]}
        characters.append(new_dict)

    characters.sort(reverse=True, key=sort_on)
    return characters


