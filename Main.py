"""
    Calculator program
    Author: Mateus Galdino
"""

import re

print("Our magical calculator")
print("Type new to reset the calculator")
print("Type quit to exit")

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    safe_input = previous

    if equation == 'quit':
        run = False
        print("Exiting calculator")
    elif equation == 'new':
        previous = 0
    else:
        equation = re.sub('[a-zA-z,.:()" "|^~´{}@#$%¨&!]', "", equation)
        try:
            if previous == 0:
                previous = eval(equation)
            else:
                previous = eval(str(previous) + equation)
        except SyntaxError:
            print("Unexpected character or end of line in equation. Please, try again")
            previous = safe_input


try:
    while run:
        perform_math()
except SyntaxError:
    print("Unexpected character or end of line. Please, try again")
    while run:
        perform_math()
