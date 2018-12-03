import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def multiset(cs):
    C = Counter()
    for _, l in cs:
        for t in l:
            C[t] += 1
    return C

def p1(cs):
    C = multiset(cs)
    return len([x for x in C.values() if x > 1])

def p2(cs):
    C = multiset(cs)
    for cid, l in cs:
        if all(C[t] == 1 for t in l):
            return cid

v = fetch(3)
claims = []
for l in v.split('\n'):
    a, _, b, c = l.split()
    cid = int(a[1:])
    x, y = map(int, b[:-1].split(','))
    w, h = map(int, c.split('x'))
    xs = []
    for i in range(x, x+w):
        for j in range(y, y+h):
            xs.append((i, j))
    claims.append((cid, xs))

print('part_1: {}'.format(p1(claims)))
print('part_2: {}'.format(p2(claims)))
