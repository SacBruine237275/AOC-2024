array = []  # Tableau global

def readFile():
    with open("input.txt") as file:
        for line in file:
            array.append(line) 

def findMas():
    result = 0
    for rowIndex, row in enumerate(array):
        for colIndex, letter in enumerate(row):
            if checkMas(rowIndex, colIndex):
                result += 1
    return result

def checkMas(row, col):
    try:
        return (
            #   M . M
            #   . A .
            #   S . S
            (array[row - 1][col - 1] == 'M' and 
             array[row - 1][col + 1] == 'M' and
             array[row][col] == 'A' and 
             array[row + 1][col - 1] == 'S' and 
             array[row + 1][col + 1] == 'S') or 
            #   S . S
            #   . A .
            #   M . M
            (array[row - 1][col - 1] == 'S' and 
             array[row - 1][col + 1] == 'S' and
             array[row][col] == 'A' and 
             array[row + 1][col - 1] == 'M' and 
             array[row + 1][col + 1] == 'M') or
            #   S . M
            #   . A .
            #   S . M
            (array[row - 1][col - 1] == 'S' and 
             array[row - 1][col + 1] == 'M' and
             array[row][col] == 'A' and 
             array[row + 1][col - 1] == 'S' and 
             array[row + 1][col + 1] == 'M') or
            #   M . S
            #   . A .
            #   M . S
            (array[row - 1][col - 1] == 'M' and 
             array[row - 1][col + 1] == 'S' and
             array[row][col] == 'A' and 
             array[row + 1][col - 1] == 'M' and 
             array[row + 1][col + 1] == 'S')
        )
    except:
        return False

# Main
def main():
    readFile()
    print(findMas())

main()
