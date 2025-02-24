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
