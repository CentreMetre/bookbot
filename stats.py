def get_num_words(text):
    words = text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")
    return num_words

def get_num_chars(text):
    char_count = {}
    for c in text:
        c = c.lower()
        if c in char_count:
            char_count[c] += 1
        if c not in char_count:
            char_count[c] = 1
    print(char_count)
    return char_count

def sort_chars(chars):
    sorted = []
    for c in chars:
        char = {"char": c, "count": chars[c]}
        sorted.append(char)

    sorted.sort(key=lambda x: x["count"], reverse=True)
    return sorted

