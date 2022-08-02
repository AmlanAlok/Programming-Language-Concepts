"""
Name: Amlan Alok
StudentID: 1001855861
Date: 2nd August, 2022
OS: maxOS Big Sur Version 11.5.1 M1 Chip
Python Version: 3.9.2
"""

import random
import math as m


def tab(space):
    gap = ''
    while space > 0:
        gap += ' '
        space -= 1
    return gap


def init_program():
    print(tab(28) + 'AMAZING PROGRAM')
    print(tab(15) + 'CREATIVE COMPUTING MORRISTOWN, NEW JERSEY')
    print('\n')

    # width, length = 10, 10

    # print(width, length)
    width, length = fetch_user_input()
    while width <= 1 or length <= 1:
        print('Meaningles Dimensions. Try Again.')
        width, length = fetch_user_input()
    return width, length


def fetch_user_input():
    user_input = input('WHAT ARE YOUR WIDTH AND LENGTH? (FOR EXAMPLE TYPE 10,10 AND PRESS ENTER)\n')
    width, length = user_input.split(',')
    width, length = int(width), int(length)
    return width, length

def init_arrays(h, v2):
    w, v = [], []
    w.append([None] * v2)
    v.append([None] * v2)
    i = 1
    while i <= h:
        w.append([])
        v.append([])
        j = 1
        w[i].append(None)
        v[i].append(None)
        while j <= v2:
            w[i].append(0)
            v[i].append(0)
            j += 1
        i += 1

    return w, v


def first_line(x, h):
    l = ''
    i = 1
    while i <= h:
        if i == x:
            l += '.  '
        else:
            l += '.--'
        i += 1
    # l += '.\n'
    l += '.'
    print(l)


def search_non_explored_cell(r, h, s, v2):
    if r < h:
        r += 1
    elif s < v2:
        r = 1
        s += 1
    else:
        r, s = 1, 1

    return r, s


def maze_logic(x, w, v, h, v2):

    q, z = 0, 0
    c = 1
    w[x][1] = c
    c += 1
    r, s = x, 1
    entry = 0

    while True:
        if entry == 2:
            r, s = search_non_explored_cell(r, h, s, v2)
            while w[r][s] == 0:
                r, s = search_non_explored_cell(r, h, s, v2)

        if entry == 0 and r-1 > 0 and w[r-1][s] == 0:

            if s-1 > 0 and w[r][s-1] == 0:
                if r<h and w[r+1][s] == 0:
                    x = m.floor(random.random()*3+1)
                elif s < v2:
                    if w[r][s+1] == 0:
                        x = m.floor(random.random() * 3 + 1)
                        if x == 3:
                            x = 4
                    else:
                        x = m.floor(random.random() * 2 + 1)
                elif z == 1:
                    x = m.floor(random.random() * 2 + 1)
                else:
                    q = 1
                    x = m.floor(random.random() * 3 + 1)
                    if x == 3:
                        x = 4
            elif r < h and w[r+1][s] == 0:
                if s < v2:
                    if w[r][s + 1] == 0:
                        x = m.floor(random.random() * 3 + 1)
                    else:
                        x = m.floor(random.random() * 2 + 1)
                    if x >= 2:
                        x += 1
                elif z == 1:
                    x = m.floor(random.random() * 2 + 1)
                    if x >= 2:
                        x += 1
                else:
                    q = 1
                    x = m.floor(random.random() * 3 + 1)
                    if x >= 2:
                        x += 1
            elif s < v2:
                if w[r][s + 1] == 0:
                    x = m.floor(random.random() * 2 + 1)
                    if x == 2:
                        x = 4
                else:
                    x = 1
            elif z == 1:
                x = 1
            else:
                q = 1
                x = m.floor(random.random() * 2 + 1)
                if x == 2:
                    x = 4
        elif s-1 > 0 and w[r][s-1] == 0:
            if r < h and w[r + 1][s] == 0:
                if s < v2:
                    if w[r][s + 1] == 0:
                        x = m.floor(random.random() * 3 + 2)
                    else:
                        x = m.floor(random.random() * 2 + 2)
                elif z == 1:
                    x = m.floor(random.random() * 2 + 2)
                else:
                    q = 1
                    x = m.floor(random.random() * 3 + 2)
            elif s < v2:
                if w[r][s + 1] == 0:
                    x = m.floor(random.random() * 2 + 2)
                    if x == 3:
                        x = 4
                else:
                    x = 2
            elif z == 1:
                x = 2
            else:
                q = 1
                x = m.floor(random.random() * 2 + 2)
                if x == 3:
                    x = 4

        elif r < h and w[r+1][s] == 0:
            if s < v2:
                if w[r][s+1] == 0:
                    x = m.floor(random.random() * 2 + 3)
                else:
                    x = 3
            elif z == 1:
                x = 3
            else:
                q = 1
                x = m.floor(random.random() * 2 + 3)
        elif s < v2:
            if w[r][s + 1] == 0:
                x = 4
            else:
                entry = 2
                continue
        elif z == 1:
            entry = 2 # Blocked
            continue
        else:
            q = 1
            x = 4

        if x == 1:
            w[r-1][s] = c
            c += 1
            v[r-1][s] = 2
            r -= 1
            if c == h * v2 + 1:
                break
            q = 0
            entry = 0
        elif x == 2:
            w[r][s-1] = c
            c += 1
            v[r][s-1] = 1
            s -= 1
            if c == h * v2 + 1:
                break
            q = 0
            entry = 0
        elif x == 3:
            w[r + 1][s] = c
            c += 1
            if v[r][s] == 0:
                v[r][s] = 2
            else:
                v[r][s] = 3
            r += 1
            if c == h * v2 + 1:
                break
            entry = 1
        elif x == 4:
            if q != 1:
                w[r][s + 1] = c
                c+=1
                if v[r][s] == 0:
                    v[r][s] = 1
                else:
                    v[r][s] = 3
                s+=1
                if c == h * v2 + 1:
                    break
                entry = 0
            else:
                z = 1
                if v[r][s] == 0:
                    v[r][s] = 1
                    q = 0
                    r = 1
                    s = 1
                    while w[r][s] == 0:
                        if r < h:
                            r += 1
                        elif s < v2:
                            r = 1
                            s += 1
                        else:
                            r = 1
                            s = 1
                    entry = 0
                else:
                    v[r][s] = 3
                    q = 0
                    entry = 2

    return v


def print_maze(v, h, v2):
    j = 1
    while j <= v2:
        st = 'I'
        i = 1
        while i <= h:
            if v[i][j] < 2:
                st += '  I'
            else:
                st += '   '
            i += 1

        print(st)

        st = ''
        i = 1
        while i <= h:
            if v[i][j] == 0 or v[i][j] == 2:
                st += ':--'
            else:
                st += ':  '
            i += 1
        print(st + '.')
        j += 1


def main():
    h, v2 = init_program()
    w, v = init_arrays(h, v2)

    x = m.floor(random.random() * h + 1)
    first_line(x, h)

    v = maze_logic(x, w, v, h, v2)

    print_maze(v, h, v2)


if __name__ == '__main__':
    main()
