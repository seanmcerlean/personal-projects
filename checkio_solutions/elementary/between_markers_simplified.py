import re

def escape_char(marker: str) -> str:
    return "\\" + marker if marker in '[]()+*' else marker
        
        
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    re.purge()
    regex = escape_char(begin) + r'(.*)' + escape_char(end)
    pattern = re.compile(regex)
    m = pattern.search(text)
    result = m.group(1) if m and m.group(1) else ''
    return result


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
