"""
Name: Amlan Alok
StudentID: 1001855861
Date:
OS: maxOS Big Sur Version 11.5.1 M1 Chip
"""

import os


def rpn(line):
    line_data = line.split()
    # print(line_data)
    stack = []

    for x in line_data:
        x_ascii = ord(x)

        if 48 <= x_ascii <= 57:
            stack.append(int(x))
        else:
            b, a = stack.pop(), stack.pop()
            if x == '+':
                z = a+b
            elif x == '*':
                z = a*b
            elif x == '-':
                z = a-b
            elif x == '/':
                z = a/b
            else:
                print('Invalid operation provided for input =', x)
                return
            stack.append(z)

    return stack[0]


def main():

    current_directory = os.getcwd()
    input_filename = 'input_RPN.txt'

    full_path = os.path.join(current_directory, input_filename)

    with open(full_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            ans = rpn(line)
            print(ans)
    f.close()


if __name__ == '__main__':
    main()