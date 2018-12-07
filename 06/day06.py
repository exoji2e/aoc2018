import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def cnt(D, x0, x1, y0, y1):
    C = [0]*len(D)
    for r, c in coords(x0, x1, y0, y1):
        M1 = (10000, -1)
        M2 = (10000, -1)
        for i, (xx, yy) in enumerate(D):
            can = (abs(r-xx) + abs(c - yy), i)
            if can < M1:
                M2 = M1
                M1 = can
            elif can < M2:
                M2 = can
        if M1[0] != M2[0]:
            C[M1[1]] += 1
    return C

def coords(x0, x1, y0, y1):
    for i in range(x0, x1):
        for j in range(y0, y1):
            yield i, j

def parse(v):
    D = []
    mx, my = 0, 0
    for i, line in enumerate(v.strip().split('\n')):
        x, y = map(int, line.split(','))
        D.append((x,y))
        mx = max(mx, x)
        my = max(my, y)
    return D, mx, my


def p1(v):
    D, mx, my = parse(v)
    v1 = cnt(D, 0, mx, 0, my)
    v2 = cnt(D, -1, mx+1, -1, my+1)
    M = 0
    for a, b in zip(v1, v2):
        if a == b:
            M = max(M, a)
    return M

def p2(v, maxV=10000):
    D, mx, my = parse(v)
    C = 0
    for x, y in coords(0, mx, 0, my):
        S = 0
        for xx, yy in D:
            S += abs(x-xx) + abs(y-yy)
        if S < maxV:
            C += 1
    return C

if __name__ == '__main__':
    v = fetch(6)
    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
    T = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""
    assert p2(T, 32) == 16
