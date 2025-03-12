from art import logo
import os

print(logo)

def calculate(first_num, second_num, operator):
    first_num = float(first_num)
    second_num = float(second_num)
    if operator == "+":
        answer = first_num + second_num
    elif operator == "-":
        answer = first_num - second_num
    elif operator == "*":
        answer = first_num * second_num
    elif operator == "/":
        answer = first_num / second_num
    
    return answer


first_num = input("What's the first number?: ")
operator = input("+\n-\n*\n/\nPick an operation: ")
second_num = input("What's the next number?: ")

answer = calculate(first_num, second_num, operator)
print(f"{first_num} {operator} {second_num} = {answer}")

still_calculate = True

while still_calculate:
    should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if should_continue == "y":
        operator = input("+\n-\n*\n/\nPick an operation: ")
        second_num = input("What's the next number?: ")
        new_answer = calculate(answer, second_num, operator)
        print(f"{answer} {operator} {second_num} = {new_answer}")
    else:
        still_calculate = False
        os.system("clear")
        