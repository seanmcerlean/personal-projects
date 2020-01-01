def calculate_indexes(text: str, begin: str, end: str) -> tuple:
    try:
        left_index = text.index(begin) + len(begin)
    except ValueError:
        left_index = 0
    try:
        right_index = text.index(end)
    except ValueError:
        right_index = len(text)
    
    return(left_index, right_index)

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    begin = begin if begin else text[0]
    end = end if end else text[-1]
    
    indexes = calculate_indexes(text, begin, end)
    
    return text[indexes[0]:indexes[1]] if indexes[0] < indexes[1] else ''


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
