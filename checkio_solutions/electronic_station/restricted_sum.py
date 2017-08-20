#https://py.checkio.org/mission/restricted-sum

def checkio(data):
    if data:
        return data[0] + checkio(data[1:])
    else:
        return 0


checkio([1, 2, 3]) == 6
checkio([2, 2, 2, 2, 2, 2]) == 12
