def checkio(data):
    #replace this for solution
    numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    
    roman = '' 
    for number in sorted(numerals.keys(), reverse=True):
        while data >= number:
            data = data - number
            roman = roman + numerals[number]
        
    return roman

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
