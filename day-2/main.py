import os

size = 100


#move dial to left
def move_left(dial):
    dial = (dial - 1) % size
    print(str(dial) + " moved to left")
    return dial

#move dial to right
def move_right(dial):
    dial = (dial + 1) % size
    print(str(dial) + " moved to right")
    return dial

#main function
def processInput():
       with open("input.txt") as file:
            dial = 50
            numberOf0s = 0
            print("The current number of zeros at the start is [" + str(numberOf0s) + "]")
            lines = file.readlines()
            for line in lines:
                if line.startswith("L"):
                    remove_letter=line[1:]
                    numberToMove = int(remove_letter) + 1
                    for i in range(1, int(numberToMove)):
                        dial = (move_left(dial))
                        if dial == 0:
                            numberOf0s += 1
                            print("The number of 0s is" + str(numberOf0s))
                else:
                    remove_letter=line[1:]
                    numberToMove = int(remove_letter) + 1
                    for i in range(1, int(numberToMove)):
                        dial = (move_right(dial))
                        if dial == 0:
                            numberOf0s += 1
                            print("The number of 0s is" + str(numberOf0s))
                    

            print("The number of zeros at the end is [" + str(numberOf0s) + "]")

                        
processInput()
