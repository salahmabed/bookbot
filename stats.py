def sort_on(items):
    return items["num"]

def bag_dicts(dict):
    bag_of_dicts = []
    for entry in dict:
        this_dict = {}
        this_dict["name"] = entry
        this_dict["num"] = dict[entry]
        bag_of_dicts.append(this_dict)

    return bag_of_dicts

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

def dict_to_sorted_array(dict):
    char_dict = get_num_chars(dict)

    dict_bag = bag_dicts(char_dict)
    dict_bag.sort(reverse=True, key=sort_on)

    return dict_bag