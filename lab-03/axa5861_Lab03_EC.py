"""
Name: Amlan Alok
StudentID: 1001855861
Date: 25th July, 2022
OS: maxOS Big Sur Version 11.5.1 M1 Chip
Python Version: 3.9.2
"""

""" The additional operator added here is the modulo division (%)"""
import os


def main():

    current_directory = os.getcwd()
    input_filename = 'input_RPN_EC.txt'
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '%': lambda a, b: a % b
    }

    full_path = os.path.join(current_directory, input_filename)

    with open(full_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            postfix = infix_to_rpn(line)
            print(postfix)
            ans = rpn(postfix, operations)
            print(ans)
    f.close()


def infix_to_rpn(line):
    line_data = line.split()
    stack = []
    operator_priority = {
        '-': 0,
        '+': 1,
        '*': 2,
        '/': 3,
        '%': 4
    }
    rpn = ''

    for x in line_data:
        if '0' <= x <= '9':
            rpn += x
        elif x == '(':
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                rpn += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and operator_priority[x] <= operator_priority[stack[-1]]:
                rpn += stack.pop()
            stack.append(x)
    while stack:
        rpn += stack.pop()
    return ' '.join(rpn)


def rpn(line, operations):
    line_data = line.split()
    stack = []

    for x in line_data:

        if x in operations:
            b, a = stack.pop(), stack.pop()
            result = operations[x](a, b)
            stack.append(result)
        elif '0' <= x <= '9':
            stack.append(int(x))
        else:
            print('Invalid operation provided for input =', x)
            return
    return stack[0]


if __name__ == '__main__':
    main()