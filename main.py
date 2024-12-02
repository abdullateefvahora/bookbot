def main():
    books_path = 'books/frankenstein.txt'
    text = readFileContents(books_path)
    num_words = countWords(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {books_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item['char'].isalpha():
            continue
        else:
            print(f'The {item['char']} character was found {item['num']} times')

    print('--- End report ---')


def readFileContents(text_path):
    with open(text_path) as f:
        return f.read()

def countWords(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        cLowered = c.lower()
        if cLowered in chars:
            chars[cLowered] += 1
        else:
            chars[cLowered] = 1
    return chars

def sort_on(d):
    return d['num']

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []

    for ch in chars_dict:
        sorted_list.append({'char': ch, 'num': chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

main()