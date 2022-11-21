import math

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    infile = open(filename, "r")

    print("File opened.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    return num1 / num2

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print("Please enter a valid number to divide.")
        raise TypeError("int or float input only")
    
    try:
        div = num1 / num2
        print("Your numbers divided is:", div)
    except:
        print("Numbers cannot be divided by zero.")
        raise ZeroDivisionError
    

## returns the squareroot of a particular number
def sq(num):
    if type(num) == int or type(num) == float:
        try: 
            square = math.sqrt(num)
            return square
        except:
            print("Value must have a valid square root.")
            raise ValueError("number does not have a valid square root.")
    else:
        print("Value entered must be a number.")
        raise TypeError("value must be either int or float.")

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    if type(first) == str and type(middle) == str and type(last) == str:
        print("Hello!")
        print("Welcome to the program", first, middle, last)
        print("Glad to have you!")
    else:
        print("Names must be string values.")
        raise ValueError("name must be string")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    if type(index) != int:
        print("Index value must be an integer.")
        raise TypeError("index must be integer")
    try:
        value = numbers[index]
        print("Your item at", index, "index is", numbers[index])
    except:
        print("Index has a value that is larger than size of array.")
        raise IndexError("index is in array")
