def safe_pawns(pawns):
    def get_defender_positions(position):
        row = position[0]
        col = position[1]
        
        defender_col = chr(ord(col) - 1)

        defender_pos1 = chr(ord(row) - 1) + defender_col
        defender_pos2 = chr(ord(row) + 1) + defender_col
        
        return (defender_pos1, defender_pos2)
    
    safe_pawns = 0
    
    for pawn in pawns:
        defender_positions = get_defender_positions(pawn)
        if defender_positions[0] in pawns or defender_positions[1] in pawns:
            safe_pawns = safe_pawns + 1    
    
    return safe_pawns

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

