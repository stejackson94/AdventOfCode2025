import os

dial = 50
size = 100
numberOf0s = 0

def move_right(dial, steps=1):
    return (dial + steps) % size

def move_left(dial, steps=1):
    return (dial - steps) % size

def processInput():
       with open("./input.txt") as file:
              lines = file.readlines()
              for line in lines:
                     print("reading file")
                     print(line)
                     print("finished reading file")

processInput()

# def findStudent(school_file, student_name):
#         with open(school_file) as file:
#                 lines = file.readlines()
#                 is_student_in_file = False
#                 foundStudentName = ""
#                 for line in lines:
#                         #checks for user in text file but ignores case sensitivity https://www.geeksforgeeks.org/case-insensitive-string-comparison-in-python/
#                         if student_name in line.casefold():
#                                 is_student_in_file = True
#                                 foundStudentName = (line.strip("\n"))

#                 if is_student_in_file == True:
#                         print(foundStudentName)
#                 else:
#                         print("Student not found")