import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def score(x, y, gse):
    rid = x + 10
    PL = rid*y
    PL += gse
    PL *= rid
    PL = (PL//100)%10
    return PL - 5

def coords():
    for i in range(1, 301):
        for j in range(1, 301):
            yield i, j


def p1(v):
    gse = int(v)
    M = -100, -1, -1
    for i, j in coords():
        if i == 1 or j == 1 or i > 298 or j > 298: continue
        S = 0
        for x in range(3):
            for y in range(3):
                S += score(i+x, j+y, gse)
        M = max(M, (S, i, j))
    return '{},{}'.format(M[1], M[2])


def p2(v):
    gse = int(v)
    M = -100, -1, -1, -1
    for i, j in coords():
        sz = min(300 - i, 300-j) + 1
        S = 0
        for v in range(sz):
            for x in range(v+1):
                S += score(i+x, j+v, gse)
            for y in range(v):
                S += score(i+v, j + y, gse)
            M = max(M, (S, i, j, v+1))
    return '{},{},{}'.format(M[1], M[2], M[3])

if __name__ == '__main__':
    v = fetch(11)
    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
