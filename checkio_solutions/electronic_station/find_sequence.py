#https://py.checkio.org/mission/find-sequence/

def checkio(matrix):
    def contains_four_in_a_row(value, sequence):
        sequence_str = ''.join(str(c) for c in sequence)
        value_str = str(value)
        return sequence_str.find(value_str*4) + 1

    def check_diaganols(x, y, length, matrix):
        expected_value = matrix[x][y]
        for l in range(length):
            if x+l >= len(matrix) or y+l >= len(matrix):
                break
            if matrix[x+l][y+l] != expected_value:
                break
        else:
            return True

        for l in range(length):
            if x - l < 0 or y + l >= len(matrix):
                break
            if matrix[x - l][y + l] != expected_value:
                break
        else:
            print("Returning True")
            return True

        return False

    for row in matrix:
        horizontal_match = any(contains_four_in_a_row(value, row) for value in row)
        if horizontal_match:
            return True

    transposed_matrix = map(list, zip(*matrix))

    for row in transposed_matrix:
        vertical_match = any(contains_four_in_a_row(value, row) for value in row)
        if vertical_match:
            return True

    if len(matrix) < 4: return False

    height = len(matrix)
    width = len(matrix[0])
    for x in range(height):
        for y in range(width):
            diagnol_match = check_diaganols(x, y, 4, matrix)
            if diagnol_match:
                return True

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert checkio([
        [1, 5, 4, 4],
        [2, 2, 4, 1],
        [1, 4, 3, 5],
        [4, 3, 3, 2]
    ]) == True, "Extra"