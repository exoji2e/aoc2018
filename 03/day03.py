import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def multiset(cs):
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
    C = Counter()
    for _, l in claims:
        for t in l:
            C[t] += 1
    return C, claims

def p1(v):
    C, _ = multiset(v)
    return len([x for x in C.values() if x > 1])

def p2(v):
    C, cs = multiset(v)
    for cid, l in cs:
        if all(C[t] == 1 for t in l):
            return cid

if __name__ == '__main__':
    v = fetch(3)
    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
