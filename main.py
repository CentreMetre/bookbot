from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
        #print(file_text)
        return file_text

def print_report_chars(chars, file):

    print(f"""
    ============ BOOKBOT ============
    Analysing file found at {file}
    ----------- Word Count ----------
    Found 75767 total words
    --------- Character Count -------""")
    for char in chars:
        letter = char["char"]
        if letter.isalpha() is True:
            count = char["count"]
            count = str(count)
            print(f"{letter}: {count}")

    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    text = get_book_text(file)
    get_num_words(text)
    chars = get_num_chars(text)
    sorted_chars = sort_chars(chars)
    #print(sorted_chars)
    print_report_chars(sorted_chars, file)

main()