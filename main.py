import sys
from stats import *

import os

def get_book_text(file_path):
    """Takes the path to a text file and returns the text as a string.

    Keyword arguments:
    file_path -- relative file location
    """
    with open(file_path, "rb") as f:
        return f.read().decode("utf-8")
    
def book_report(file_path):
    """Opens a text file and counts the number of words and characters in it.

    Keyword arguments:
    file_path -- the file's relative location
    """
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    char_array = dict_to_sorted_array(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in char_array:
        print(f"{char_dict["name"]}: {char_dict["num"]}")
    print("============= END ===============")

def main():
    """Activates and runs the bookbot."""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_address = sys.argv[1]
        book_report(book_address)

        print("path:", os.path.abspath(book_address))
        print("stat size:", os.path.getsize(book_address))
        with open(book_address, "r", encoding="utf-8", newline=None) as f:
            print("newlines seen:", f.newlines)  # after first read attempt, so:
            text = f.read()
        print("len(text):", len(text))
        with open(book_address, "rb") as f:
            data = f.read()
        print("rb len:", len(data))
        print("decoded len:", len(data.decode("utf-8")))
        print("get_book_text from:", get_book_text.__code__.co_filename)
        
main()