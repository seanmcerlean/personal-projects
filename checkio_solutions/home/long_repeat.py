import re


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """


    if not line:
        return 0

    longest_letter_sequences = [
        len(max(re.findall('{0}+'.format(letter), line))) for letter in set(line)
    ]

    return max(longest_letter_sequences)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
