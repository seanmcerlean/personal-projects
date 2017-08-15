import re


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """

    if not line:
        return 0

    chars = set(line)
    single_char_sequences = re.findall(r"{}+".format("+|".join(chars)), line)
    single_char_sequence_lengths = map(len, single_char_sequences)
    return max(single_char_sequence_lengths)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
