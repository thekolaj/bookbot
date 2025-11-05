from stats import count_words, count_characters, sort_characters


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    num_chars = count_characters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print_char_report(sort_characters(num_chars))


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def print_char_report(char_list: list):
    print("--------- Character Count -------")
    for x in char_list:
        if not x["char"].isalpha():
            continue

        print(f"{x['char']}: {x['num']}")


main()
