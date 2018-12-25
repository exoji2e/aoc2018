import sys
sys.path.extend(['..', '.'])
from fetch import fetch, get_samples
from collections import *

def run(v, log=False):
    items = []
    MM = [500, 500, 10**5, -10**5]
    for l in v.strip('\n').split('\n'):
        a, b = l.split(', ')
        s, e = map(int,b[2:].split('..'))
        L = int(a[2:])
        if 'x' in a:
            items.append((L, L, s, e))
        else:
            items.append((s, e, L, L))
        item = items[-1]
        MM[0] = min(MM[0], item[0])
        MM[2] = min(MM[2], item[2])
        MM[1] = max(MM[1], item[1])
        MM[3] = max(MM[3], item[3])
    assert MM[0] >= 0 and MM[2] >= 0
    B = [[False]*(MM[3]+2) for _ in range(MM[1]+2)]
    ORIG = set()
    for x0, x1, y0, y1 in items:
        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                B[x][y] = True
                ORIG.add((x, y))
    C = set()
    def cnt():
        return len([1 for (x, y) in C if MM[2] <= y <= MM[3] and (x, y) not in ORIG])
    while True:
        L = cnt()
        flows = [(500, 0)]
        seen = set()
        while flows:
            START = flows.pop()
            x, y = START
            Y = y
            if B[x][y]:
                continue
            while not B[x][y]:
                C.add((x, y))
                y += 1
                if y >= MM[3]+1:
                    break
            if y >= MM[3]+1: continue
            y -= 1
            X = x
            while B[x][y+1]:
                x-=1
                if B[x][y]:
                    break
            X0 = x + 1
            x = X
            while B[x][y+1]:
                x += 1
                if B[x][y]:
                    break
            X1 = x - 1
            for x in range(X0, X1+1):
                C.add((x, y))
            if B[X0-1][y] and B[X1+1][y]:
                for x in range(X0, X1+1):
                    B[x][y] = True
                flows.append(START)
            else:
                if Y < y:
                    if not B[X0-1][y]:
                        x, y = X0 -1, y
                        if (x, y) not in seen:
                            seen.add((x, y))
                            flows.append((x, y))
                    if not B[X1+1][y]:
                        x, y = X1+1, y
                        if (x, y) not in seen:
                            seen.add((x, y))
                            flows.append((x, y))
        if L == cnt():
            break
    S = 0
    for x in range(len(B)):
        for y in range(len(B[0])):
            if B[x][y] and not (x, y) in ORIG:
                S += 1
    return cnt(), S

def p1(v):
    return run(v)[0]

def p2(v):
    return run(v)[1]

if __name__ == '__main__':
    DAY = 17
    for fname, data in get_samples(DAY):
        assert p1(data) == 57
        assert p2(data) == 29
    v = fetch(DAY)

    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
