from collections import Counter

def checkio(text):
    letter_counts = Counter(text.lower()).most_common()
    letter_counts = list(filter(lambda t: t[0].isalpha(), letter_counts))
    max_count = max(letter_counts, key=lambda x: x[1])[1]
    max_letters = [count[0] for count in letter_counts if count[1] == max_count]
    return min(max_letters) if max_letters else None


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
