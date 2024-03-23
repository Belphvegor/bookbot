def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def get_book_word_counts(content):
    words = content.split()
    return len(words)


def count_letters(words):
    letter_count = {}
    for word in words:
        if word in letter_count:
            letter_count[word] += 1
        else:
            letter_count[word] = 1
    return letter_count


def report(path):
    text = get_book_text(path)
    num_words = get_book_word_counts(text)
    letter_words = count_letters(text)
    sorted_letter_words = dict(
        sorted(letter_words.items(), key=lambda item: item[1], reverse=True)
    )
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print("\n")
    for key, value in sorted_letter_words.items():
        if not key.isalpha():
            continue
        print(f"the '{key}' character was found {value} times")
    print(f"--- End report ---")
    pass


def main():
    books = "books/frankenstein.txt"
    report(books)


main()
