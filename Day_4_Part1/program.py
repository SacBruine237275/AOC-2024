array = [] #Tableau global
def readFile():
    numberOfLine=-1
    with open("input.txt") as file:
        for line in file:
            numberOfLine=numberOfLine+1
            array.append([])
            for letter in line:
                array[numberOfLine].append(letter)

def findXmas():
    result=0
    for row in array:
        for letter in row:
            print(letter)
    return result
def main():
    readFile()
    #print(array)
    print(findXmas())

main()