# imports
from stats import get_num_words, get_num_characters, sort_characters
import sys

def main():
    if len(sys.argv) < 2:
        print("Please use following format: Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
     book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_num_characters(text)
    character_list = sort_characters(text)
    
        
    print("============ BOOKBOT ============ ")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    
    for char in character_list:
        letter = char["char"]
        if letter.isalpha():
            print(f"{letter}: {char['num']}")
    
        
    print("============= END ==============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()