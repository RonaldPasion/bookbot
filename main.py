import sys
from stats import count_words, count_chars, sorted_list


def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python2 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted = sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()