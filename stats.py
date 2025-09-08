def get_num_words(string_of_words):
    return len(string_of_words.split())

def get_num_chars(string_of_words):
    lower_case_string = string_of_words.lower()
    char_dict = {}

    for ch in lower_case_string:
        if ch in char_dict.keys():
            char_dict[str(ch)] += 1
        else:
            char_dict[str(ch)] = 1
    return char_dict