import sys
sys.setrecursionlimit(100000) #pour pouvoir utiliser la récursivité

tableau = [] #variable global
def readFile():
    with open("input.txt", "r") as f:
        for ligne in f:
            ligne = ligne.strip() 
            tableau.append(list(ligne)) 

def searchStart():
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j] == "^":
                return (i, j)

def calculatePassageCount():
    passageCount = 0
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j] == "X":
                passageCount += 1
    return passageCount

def moveGuard(row, column):
    if(row < 0 or row >= len(tableau) or column < 0 or column >= len(tableau[0])):
        return
    if tableau[row][column] == "^":
        tableau[row][column] = "X"
        if tableau[row-1][column] == "#":
            tableau[row][column+1] = ">"
            moveGuard(row, column+1)
        else:
            tableau[row-1][column] = "^"
            moveGuard(row-1, column)
    elif tableau[row][column] == ">":
        tableau[row][column] = "X"
        if tableau[row][column+1] == "#":
            tableau[row+1][column] = "v"
            moveGuard(row+1, column)
        else:
            tableau[row][column+1] = ">"
            moveGuard(row, column+1)
    elif tableau[row][column] == "v":
        tableau[row][column] = "X"
        if tableau[row+1][column] == "#":
            tableau[row][column-1] = "<"
            moveGuard(row, column-1)
        else:
            tableau[row+1][column] = "v"
            moveGuard(row+1, column)
    elif tableau[row][column] == "<":
        tableau[row][column] = "X"
        if tableau[row][column-1] == "#":
            tableau[row-1][column] = "^"
            moveGuard(row-1, column)
        else:
            tableau[row][column-1] = "<"
            moveGuard(row, column-1)
        


def main():
    readFile()
    (startRow,startColumn)=searchStart()
    moveGuard(startRow, startColumn)
    print(calculatePassageCount())

main()