tableau = []  # Variable globale

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

def getNextPosition(row, col, direction):
    if direction == "^":
        return row - 1, col
    elif direction == ">":
        return row, col + 1
    elif direction == "v":
        return row + 1, col
    elif direction == "<":
        return row, col - 1

def turnRight(direction):
    directions = "^>v<"
    return directions[(directions.index(direction) + 1) % 4]

def simulateGuard(start_row, start_col):
    visited_states =    ()  # États visités sous forme (position, direction)
    row, col = start_row, start_col
    direction = "^"

    while True:
        current_state = (row, col, direction)
        if current_state in visited_states:
            return True  # Boucle détectée
        visited_states.add(current_state)

        next_row, next_col = getNextPosition(row, col, direction)

        if not (0 <= next_row < len(tableau) and 0 <= next_col < len(tableau[0])):
            return False

        if tableau[next_row][next_col] == "#":
            direction = turnRight(direction)  
        else:
            row, col = next_row, next_col

def countLoopingObstacles(start_row, start_col):
    """Compte les positions où un obstacle force le garde à entrer dans une boucle."""
    loop_positions = 0

    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j] in {"#", "^"} or (i == start_row and j == start_col):
                continue  # Ignorer les obstacles existants et la position de départ

            # Place un obstacle temporaire
            tableau[i][j] = "#"

            if simulateGuard(start_row, start_col):
                loop_positions += 1

            # Retire l'obstacle temporaire
            tableau[i][j] = "."

    return loop_positions

def main():
    readFile()
    start_row, start_col = searchStart()
    print(countLoopingObstacles(start_row, start_col))

main()
