def get_book_text(filepath):
    contents = ""
    with open(filepath) as file:
        contents = file.read()
    return contents

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()