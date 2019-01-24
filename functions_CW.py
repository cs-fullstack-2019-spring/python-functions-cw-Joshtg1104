def main():

    # problem1()
    # problem2()
    # problem3()
    problem4()


# ### Problem 1:
# Create a function in your program that counts from 0 to [NUMBER]

def problem1():
    counterFunction(20)

def counterFunction(number):
    for num in range(number):
        num += 1
        print(num)

# ### Problem 2:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.

def problem2():
    while True:
        ask = input("Press 'Q' to QUIT")
        if ask == 'q' or ask == 'Q':
            break
        else:
            continue

# ### Problem 3:
# Create 4 functions called add, subtract, multiply, and divide.
# Create them to allow a user to perform the name of the function to the two numbers and return the result.

def problem3():
    add(4, 6)
    sub(89, 21)
    mult(3, 28)
    div(2, 78)


def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

def mult(a, b):
    print(a * b)

def div(a, b):
    print(a / b)


# ### Problem 4:
# Create a function that will ask the user for a number.
# Use the function to get two numbers, then pass the two numbers to a function and
# ask a user if they want to add, subtract, multiple, or divide them.
# Return a string that prints the two numbers, which operation it did, and the result.

def problem4():

    print(mathFunctoin())

def mathFunctoin():
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter another number"))
    add = (num1 + num2)
    sub = (num1 - num2)
    mult = (num1 * num2)
    div = (num1 // num2)


    while True:
        ask = input("Would you like add, subtract, multiply, or divide those numbers?")
        if ask == 'divide' or ask == 'Divide':
            return f"{num1} and {num2} divided equals " + str(div)
        elif ask == 'multiply' or ask == 'Multiply':
            return f"{num1} and {num2} multiplied equals " + str(mult)
        elif ask == 'subtract' or ask == 'Subtract':
            return f"{num1} and {num2} subtracted equals " + str(sub)
        elif ask == 'add' or ask == 'Add':
            return f"The sum of {num1} and {num2} is " + str(add)
        else:
            return "ERROR. INVALID INPUT."











if __name__ == '__main__':
    main()