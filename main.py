from stats import count_words


def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(text)
    print(f"Found {word_count} total words")

main()