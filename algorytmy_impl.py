import numpy as np
import math


def PM(text, d=5, key=[3, 4, 1, 5, 2]):
    if len(text) <= 0:
        return "Nie wprowadzono tekstu"
    
    matrix = [["_" for i in range(d)] for j in range(math.ceil(len(text) / d))]

    row = 0
    for i in range(len(text)):
        matrix[row][i % d] = text[i]
        if i % d == d - 1:
            row += 1

    encrypted = ""
    row = 0
    for i in range(len(matrix)):
        for j in range(len(key)):
            # if matrix[i][key[j] - 1] != "_":
                encrypted += matrix[i][key[j] - 1]

    return encrypted


def PM_decrypt(text, d=5, key=[3, 4, 1, 5, 2]):
    if len(text) <= 0:
        return "Nie wprowadzono tekstu"
    
    matrix = [["_" for i in range(d)] for j in range(math.ceil(len(text) / d))]

    while len(text) % d != 0:
        text += "_"

    for i in range(math.ceil(len(text) / d)):
        for j in range(d):
            matrix[i][key[j] - 1] = text[i * d + j]

    matrix = np.array(matrix)
    return "".join(matrix.flatten()).replace("_", "")


def PM2(text, key_word):
    if len(text) <= 0:
        return "Nie wprowadzono tekstu"
    
    d = len(key_word)
    key = np.argsort(np.array(list(key_word)))

    matrix = [["_" for i in range(d)] for j in range(math.ceil(len(text) / d))]

    row = 0
    for i in range(len(text)):
        matrix[row][i % d] = text[i]
        if i % d == d - 1:
            row += 1

    matrix = np.array(matrix)
    matrix = matrix[:, key]
    matrix = matrix.transpose()

    result = ""
    for x in matrix:
        result += "".join(x).replace("_", "")
        result += " "

    return result


def PM2_decrypt(text, key_word):
    if len(text) <= 0:
        return "Nie wprowadzono tekstu"
    
    d = len(key_word)
    key = np.argsort(np.array(list(key_word)))

    words = text.split()
    max_col_len = max([len(x) for x in words])
    matrix = [["_" for i in range(d)] for j in range(max_col_len)]

    for i in range(len(key)):
        for j in range(len(words[i])):
            matrix[j][key[i]] = words[i][j]

    matrix = np.array(matrix)
    return "".join(matrix.flatten()).replace("_", "")


def RF1(text, key):
    col, dir_down, row, tab = data(key, text)
    if len(text) <= 0:
        return "Nie wprowadzono tekstu"
    else:
        for i in range(len(text)):

            if (row == 0) or (row == key - 1):
                dir_down = not dir_down

            tab[row][col] = text[i]
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        result = []
        for i in range(key):
            for j in range(len(text)):
                if tab[i][j] != "\n":
                    result.append(tab[i][j])
        return "".join(result)


def data(key, text):
    tab = [["\n" for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0
    return col, dir_down, row, tab


def RF2(cipher, key):
    col, dir_down, row, tab = data(key, cipher)
    if len(cipher) <= 0:
        return "Nie wprowadzono tekstu"
    else:
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            tab[row][col] = "-"
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if (tab[i][j] == "-") and (index < len(cipher)):
                    tab[i][j] = cipher[index]
                    index += 1

        result = []
        row, col = 0, 0
        for i in range(len(cipher)):

            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            if tab[row][col] != "-":
                result.append(tab[row][col])
                col += 1

            if dir_down:
                row += 1
            else:
                row -= 1
        return "".join(result)
