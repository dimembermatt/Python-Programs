#!/usr/bin/python3
#Author: Matthew Yu
#Created: 5/17/2018
#Last Updated: 5/22/2018
#This program is solely for learning the basics of Python. Topics included are
#simple IO, error checking, syntax, mathematical operations, dictionaries, lists, etc.
#PyPractice.py

#Exercise tests from practicepython.org.

#Exercise 1: Create a program that asks the user to enter their name
#and age. Output a message that tells them the year they turn 100 years old
def Exercise_1():
    print("\nExercise 1:")

    name = input("What is your name: ")
    print("Hello, " + name + ".")
    age = int(input("What is your age: "))
    print(name + " is", age, " years old.")
    print("You will be 100 years old in", 2018 - age + 100,".")

    print("\nEnd of Exercise 1.\n")
    input("Press the enter key to continue.")

#Exercise 2: Ask the user for a number and output if odd or even
#Extras: output message for multiple of 4,
#   prompt again for two numbers, check if no1 divides evenly into no2
def Exercise_2():
    print("\nExercise 2:")

    num = input("Enter a number: ")
    result = int(num) % 2
    if result == 0 :
        print(num + " is an even number.")
    else:
        print(num + " is an odd number.")

    #check if divisible by 4
    result = int(num) % 4
    if result == 0 :
        print("This number is also divisible by 4.")

    #input 2
    num = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    result = num2%num
    if result == 0 :
        print(num,"divides evenly into", num2,".")
    else :
        print(num,"does not divide evenly into", num2,".")

    print("\nEnd of Exercise 2.\n")
    input("Press the enter key to continue.")

#Exercise 2.5: Error handling from input exceptions - Ask user for specific type
#of input, if wrong type, output error message and retry.
def Exercise_2pt5():
    print("\nExercise 2.5:")

    while 1:
        try:
            num = int(input("Enter a NUMBER: "))
            break
        except ValueError:
            print("Enter only decimal numbers.")
            continue

    print("Your number is:", num)

    print("\nEnd of Exercise 2.5.\n")
    input("Press the enter key to continue.")

#Exercise 3: take a list and print out elements of the list that are less than 5
#Extras: print out results as a new list
#   ask user for number and repeat prompt with that number as qualifier
def Exercise_3():
    print("\nExercise 3:")

    testList = [1, 1, 2, 3, 5, 13, 21, 34, 55, 89]
    myList = []
    print("Your testList is:", testList)
    print("The elements in the list less than 5 are: ")
    for element in testList:
        if element < 5:
            print(element)
            myList.append(element)

    print("In list form: ", myList)

    while 1:
        try:
            qualifier = int(input("Enter a NUMBER qualifier: "))
            break
        except ValueError:
            print("Enter only decimal numbers.")
            continue

    myList2 = []
    for element in testList:
        if element < qualifier:
            myList2.append(element)

    print("The new list less than", qualifier, "are:", myList2)

    print("\nEnd of Exercise 3.\n")
    input("Press the enter key to continue")

#Exercise 4: ask for a number and print a list of all divisors of the number.
def Exercise_4():
    print("\nExercise 4:")

    while 1:
        try:
            qualifier = int(input("Enter a NUMBER qualifier: "))
            break
        except ValueError:
            print("Enter only decimal numbers.")
            continue

    resList = []
    list = range(2, qualifier)
    for elem in list:
        if qualifier%elem == 0:
            resList.append(elem)

    print("The divisors of", qualifier, "are", resList)

    print("\nEnd of Exercise 4.\n")
    input("Press the enter key to continue")

#Exercise 5: given two lists, return the elements that are duplicates.
def Exercise_5():
    print("\nExercise 5:")
    list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print("Given two lists,\nlist A:", list1,"and \nlist B:", list2)

    common = []
    for elem in list1:
        if elem in list2:
            common.append(elem)

    print("The common elements in both lists are:", common)

    print("\nEnd of Exercise 5.\n")
    input("Press the enter key to continue")

#Exercise 6: enter a string and check if it is a palindrome.
def Exercise_6():
    print("\nExercise 6:")

    string = input("Enter a string: ")
    if string == string[::-1]:
        print("This string is a palindrome.")
    else:
        print("This string is not a palindrome.")

    print("\nEnd of Exercise 6.\n")
    input("Press the enter key to continue")

#Exercise 7: given a list, output a list with only even elements.
def Exercise_7():
    print("\nExercise 7:")

    list_7 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print("Given a list:", list_7)
    nList = [x for x in list_7 if x%2 == 0]
    #del list_7[x for x in list_7 if x%2 == 1]
    print("The only even integers are:", nList)

    print("\nEnd of Exercise 7.\n")
    input("Press the enter key to continue")

#Exercise 8: rock paper scissors with player input and random input.
def Exercise_8():
    print("\nExercise 8:")

    compInp = random.randint(0, 2)
    while 1:
        try:
            userInp = int(input("Enter a NUMBER (0 for Rock, 1 for Paper, 2 for Scissors): "))
            break
        except ValueError:
            print("Enter only decimal numbers.")
            continue

    print("Player used %i, Computer used %i"% (userInp, compInp))
    if compInp == userInp:
        print("It's a tie!")
    elif ((compInp == 1 and userInp == 2) or (compInp == 2 and userInp == 0) or (compInp == 0 and userInp == 1)):
        print("Player Wins!")
    else:
        print("Computer Wins!")


    print("\nEnd of Exercise 8.\n")
    input("Press the enter key to continue")

#Exercise 9: computer generates a number and the player guesses the number.
def Exercise_9():
    print("\nExercise 9:")

    num = random.randint(0, 10)
    inp = -1

    while num != inp:
        while 1:
            try:
                inp = int(input("Guess the number! (0-10, -2 to esc):"))
                break
            except ValueError:
                print("Enter only decimal numbers.")
                continue
        if inp == -2:
            print("Exiting...")
            break
        elif num < inp:
            print("Smaller!")
        elif num > inp:
            print("Larger!")
        elif num == inp:
            print("You got it!")


    print("\nEnd of Exercise 9.\n")
    input("Press the enter key to continue")

#Exercise 10: redo of exercise 5 using list comprehensions and randomInt.
def Exercise_10():
    print("\nExercise 10:")

    list1 = random.sample(range(50), 15)
    list2 = random.sample(range(50), 15)
    print("Given two lists,\nlist A:", list1,"and \nlist B:", list2)

    common = [elem for elem in list1 if elem in list2]
    print("The common elements in both lists are:", common)

    print("\nEnd of Exercise 10.\n")
    input("Press the enter key to continue")

#Exercise 11: ask for a number and check if prime.
def getNum():
    while 1:
        try:
            inp = int(input("Give me a NUMBER:"))
            break
        except ValueError:
            print("Enter only decimal numbers.")
            continue
    return inp
def Exercise_11():
    print("\nExercise 11:")

    num = getNum()
    bool = 0
    factors = []
    for x in range(2, num):
        if num%x == 0:
            bool = 1
            factors.append(x)

    if bool == 0:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number. Its factors are:", factors)

    print("\nEnd of Exercise 11.\n")
    input("Press the enter key to continue")

#Exercise 14: take a list and remove all duplicate elements.
def Exercise_14():
    print("\nExercise 14:")

    list = random.sample(range(25), 15)
    mySet = set(list)
    print("Your random list is:\n", list, "\nYour set is:\n", mySet)

    print("\nEnd of Exercise 14.\n")
    input("Press the enter key to continue")

#Exercise 15: take a sentence and repeat it backwards.
def Exercise_15():
    print("\nExercise 15:")

    sentence = input("Enter a sentence:")
    sentence = sentence.split()
    nSentence = " ".join(sentence[::-1])
    print("Your sentence reversed is:",nSentence)


    print("\nEnd of Exercise 15.\n")
    input("Press the enter key to continue")


#setup dictionary
exercises = {
    1:      Exercise_1,
    2:      Exercise_2,
    2.5:    Exercise_2pt5,
    3:      Exercise_3,
    4:      Exercise_4,
    5:      Exercise_5,
    6:      Exercise_6,
    7:      Exercise_7,
    8:      Exercise_8,
    9:      Exercise_9,
    10:     Exercise_10,
    11:     Exercise_11,
    14:     Exercise_14,
    15:     Exercise_15,
}

#Hello World start
import random
print("Hello, python!")
input("Press the enter key to continue.")

while 1:
    print("Current dictionary of exercises:")
    for element in exercises:
        print(exercises[element])
    while 1:
        try:
            ExerciseInp = int(input("Enter a NUMBER that is an Exercise to perform. Else '-1' to exit. "))
            break
        except ValueError:
            print("Enter only decimal numbers.")
            continue
    if ExerciseInp == -1:
        exit()
    elif ExerciseInp in exercises:
        print("Executing Exercise", ExerciseInp,".")
        exercises[ExerciseInp]()
    else:
        print("Exercise is not in the Exercises dictionary.\n")
