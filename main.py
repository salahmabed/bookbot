from stats import *

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_address = "books/frankenstein.txt"
    print(get_num_words(get_book_text(book_address)))
    print(get_num_chars(get_book_text(book_address)))

main()