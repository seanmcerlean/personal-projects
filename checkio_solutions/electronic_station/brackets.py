# https://py.checkio.org/mission/brackets/

def checkio(expression):
    bracket_match = {']': '[', '}': '{', ')': '('}
    bracket_stack = []

    for char in expression:
        if char in ('[', '{', '('):
            bracket_stack.append(char)
        elif char in (']', '}', ')'):
            if not bracket_stack:
                return False
            elif bracket_stack[-1] != bracket_match[char]:
                return False
            else:
                bracket_stack.pop()

    # If the list is empty all brackets matched
    return not bracket_stack


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
