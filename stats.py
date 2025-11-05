def count_words(text: str) -> int:
    arr = text.split()
    return len(arr)


def count_characters(text: str) -> dict:
    char_map = {}

    for char in text.lower():
        char_map[char] = char_map.get(char, 0) + 1

    return char_map


def sort_characters(char_map: dict) -> dict:
    sorted_chars = []

    for char in char_map:
        sorted_chars.append({"char": char, "num": char_map[char]})

    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars


def sort_on(items):
    return items["num"]
