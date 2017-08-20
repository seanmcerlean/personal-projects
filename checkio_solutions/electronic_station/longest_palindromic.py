# https://py.checkio.org/mission/the-longest-palindromic
def longest_palindromic(text):
    length = len(text)
    substring_gen = (text[i:j+1] for i in range(length) for j in range(length))
    is_palindrome = lambda word: word == word[::-1]

    current_longest = ''
    for substring in substring_gen:
        if is_palindrome(substring) and len(substring) > len(current_longest):
            current_longest = substring

    return current_longest

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
