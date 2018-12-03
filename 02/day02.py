import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def p1(ws):
    x, y = 0, 0
    for w in ws:
        C = Counter()
        for c in w: C[c] += 1
        if 2 in set(C.values()): x += 1
        if 3 in set(C.values()): y += 1
    return x*y

def p2(ws):
    for w1 in ws:
        for w2 in ws:
            common = ''
            for c1, c2 in zip(w1, w2):
                if c1 == c2:
                    common += c1
            if len(common) == len(w1) - 1:
                return common

v = fetch(2).split()

print('part_1: {}'.format(p1(v)))
print('part_2: {}'.format(p2(v)))
