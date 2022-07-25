"""
Name: Amlan Alok
StudentID: 1001855861
Date:
OS: maxOS Big Sur Version 11.5.1 M1 Chip
"""

import os


def main():
    read_file('input_RPN.txt')


def read_file(filename):
    current_directory = os.getcwd()
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    full_path = os.path.join(current_directory, filename)

    with open(full_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            ans = rpn(line, operations)
            print(ans)
    f.close()


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