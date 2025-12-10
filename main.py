from stats import count_words, count_chars


def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(text)
    char_count = count_chars(text)
    print(f"Found {word_count} total words")
    print(char_count)

main()