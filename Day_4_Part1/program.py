array = []  # Tableau global
word = "XMAS"

def readFile():
    with open("input.txt") as file:
        for line in file:
            array.append([char for char in line.strip()])  # Enlève les espaces et les sauts de ligne inutiles

def findXmas():
    result = 0
    for rowIndex, row in enumerate(array):
        for colIndex, letter in enumerate(row):
            # Vérifie toutes les directions
            if checkLeft(rowIndex, colIndex):
                result += 1
            if checkRight(rowIndex, colIndex):
                result += 1
            if checkUp(rowIndex, colIndex):
                result += 1
            if checkDown(rowIndex, colIndex):
                result += 1
            if checkDiagonalTopLeft(rowIndex, colIndex):
                result += 1
            if checkDiagonalTopRight(rowIndex, colIndex):
                result += 1
            if checkDiagonalBottomLeft(rowIndex, colIndex):
                result += 1
            if checkDiagonalBottomRight(rowIndex, colIndex):
                result += 1
    return result


def checkLeft(row, col):
    if col - len(word) + 1 < 0:
        return False
    for i in range(len(word)):
        if array[row][col - i] != word[i]:
            return False
    return True

def checkRight(row, col):
    if col + len(word) > len(array[row]):
        return False
    for i in range(len(word)):
        if array[row][col + i] != word[i]:
            return False
    return True

def checkUp(row, col):
    if row - len(word) + 1 < 0:
        return False
    for i in range(len(word)):
        if array[row - i][col] != word[i]:
            return False
    return True

def checkDown(row, col):
    if row + len(word) > len(array):
        return False
    for i in range(len(word)):
        if array[row + i][col] != word[i]:
            return False
    return True

def checkDiagonalTopLeft(row, col):
    if row - len(word) + 1 < 0 or col - len(word) + 1 < 0:
        return False
    for i in range(len(word)):
        if array[row - i][col - i] != word[i]:
            return False
    return True

def checkDiagonalTopRight(row, col):
    if row - len(word) + 1 < 0 or col + len(word) > len(array[row]):
        return False
    for i in range(len(word)):
        if array[row - i][col + i] != word[i]:
            return False
    return True

def checkDiagonalBottomLeft(row, col):
    if row + len(word) > len(array) or col - len(word) + 1 < 0:
        return False
    for i in range(len(word)):
        if array[row + i][col - i] != word[i]:
            return False
    return True

def checkDiagonalBottomRight(row, col):
    if row + len(word) > len(array) or col + len(word) > len(array[row]):
        return False
    for i in range(len(word)):
        if array[row + i][col + i] != word[i]:
            return False
    return True

# Main
def main():
    readFile()
    print(findXmas())

main()
