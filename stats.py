def word_count(text):
    words = text.split()
    return len(words)


def char_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict


def sort_char_count(text):
    char_dict = char_count(text)
    sorted_chars = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        print(f"{char}: {count}")
