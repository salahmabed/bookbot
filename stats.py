def sort_on(items):
    """ Returns the value of the "num" key in an dictionary's items. """
    return items["num"]

def bag_dicts(some_dict):
    """Convert a dictionary into an array of dictionaries, where each entry has a "name" key and a "num" key.

    Keyword arguments:
    some_dict -- dictionary to be sorted
    """
    bag_of_dicts = []
    for this_name, this_num in some_dict.items():
        this_dict = {}
        this_dict["name"] = this_name
        this_dict["num"] = this_num
        bag_of_dicts.append(this_dict)

    return bag_of_dicts

def get_num_words(string_of_words):
    """ Splits the inputted string into a number of words, then counts those words. """
    return len(string_of_words.split())

def get_num_chars(string_of_words):
    """Converts a string into a dictionary of letters and number of instances of each letter.

    Keyword arguments:
    string_of_words -- string to be broken down
    """
    lower_case_string = string_of_words.lower()
    char_dict = {}

    for ch in lower_case_string:
        if ch.isalpha():
            if "a" <= ch <= "z":
                if ch in char_dict.keys():
                    char_dict[str(ch)] += 1
                else:
                    char_dict[str(ch)] = 1
    
    return char_dict

def dict_to_sorted_array(some_dict):
    """Converts a dictionary into an array, sorted by order of the dictionary's keys.

    Keyword arguments:
    some_dict -- dictionary to be inputted
    """
    char_dict = get_num_chars(some_dict)

    dict_bag = bag_dicts(char_dict)
    dict_bag.sort(reverse=True, key=sort_on)

    return dict_bag