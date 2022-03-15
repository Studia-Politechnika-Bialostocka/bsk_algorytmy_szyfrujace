import numpy as np
import math


def PM(text, d = 5, key = [3, 4, 1, 5, 2]):
    matrix = [['_' for i in range(d)] for j in range(math.ceil(len(text)/d))]

    row = 0
    for i in range(len(text)):
        matrix[row][i%d] = text[i]
        if i%d == d-1:
            row += 1

    encrypted = ''

    row = 0
    for i in range(len(matrix)):
        for j in range(len(key)):
            if matrix[i][key[j]-1] != '_':
                encrypted += matrix[i][key[j]-1]

    return encrypted


def PM2(text, key_word):
    d = len(key_word)
    key = np.argsort(np.array(list(key_word)))

    matrix = [['_' for i in range(d)] for j in range(math.ceil(len(text)/d))]

    row = 0
    for i in range(len(text)):
        matrix[row][i%d] = text[i]
        if i%d == d-1:
            row += 1

    matrix = np.array(matrix)
    matrix = matrix[:, key]
    matrix = matrix.transpose()
    
    result = ''
    for x in matrix:
        result += ''.join(x).replace('_', '')
        result += ' '

    return result