import sys
sys.path.extend(['..', '.'])
from fetch import fetch, get_samples
from collections import *

def find(u, ps):
    while ps[u] != u:
        u = ps[u]
    return u

def union(u, v, ps, sz):
    uR = find(u, ps)
    vR = find(v, ps)
    if uR == vR:
        return False
    if sz[uR] < sz[vR]:
        ps[uR] = vR
        sz[vR] += sz[uR]
    else:
        ps[vR] = uR
        sz[uR] += sz[vR]
    return True

def D(p1, p2):
    return sum([abs(p1[i] - p2[i]) for i in range(4)])

def p1(v, log=False):
    coords = []
    for line in v.split('\n'):
        coords.append(tuple(map(int, line.split(','))))
    n = len(coords)
    ps = [i for i in range(n)]
    sz = [1]*n
    for i in range(n):
        for j in range(i+1, n):
            if D(coords[i], coords[j]) <= 3:
                union(i, j, ps, sz)
    return len([x for i, x in enumerate(ps) if i == x])

def p2(v, log=False):
    return 0

if __name__ == '__main__':
    DAY=25
    ans = {'1.in': 2, '2.in': 4, '3.in': 3, '4.in' : 8}
    for fname, data in get_samples(DAY):
        assert p1(data) == ans[fname.split('/')[-1]]
    v = fetch(DAY)

    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
