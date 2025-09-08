from stats import *

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def book_report(file_path):
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    char_array = dict_to_sorted_array(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in char_array:
        if char_dict["name"].isalpha():
            print(f"{char_dict["name"]}: {char_dict["num"]}")
    print("============= END ===============")

def main():
    book_address = "books/frankenstein.txt"
    book_report(book_address)

main()