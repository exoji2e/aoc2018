import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def get_next(x, y, i, dx, dy, b, turns):
    if b[x][y] == '+':
        turns[i] = (turns[i] + 1)%3
        if turns[i] == 0:
            dx, dy = dy, -dx
        elif turns[i] == 1:
            dx, dy = -dy, dx
    elif b[x][y] == '/':
        dx, dy = -dy, -dx
    elif b[x][y] == '\\':
        dx, dy = dy, dx
    else:
        assert b[x][y] in '|-'
        if b[x][y] == '|': assert abs(dx) == 1 and dy == 0
        if b[x][y] == '-': assert abs(dx) == 0 and abs(dy) == 1
    nx, ny = x+dx, y+dy
    return nx, ny, dx, dy


def get_carts(b):
    carts = []
    pos = defaultdict(list)
    dxdy = {'>': (0, 1),
            '<': (0, -1),
            'v': (1, 0),
            '^': (-1, 0)}
    for i, line in enumerate(b):
        for j, ch in enumerate(line):
            T = len(carts)
            if ch not in '><^v': continue
            carts.append((i, j, T, dxdy[ch]))
            if ch in '<>':
                line[j] = '-'
            else:
                line[j] = '|'
            pos[i,j].append(T)
    return carts, pos

def p1(v):
    b = [list(x) for x in v.split('\n')]
    carts, pos = get_carts(b)
    turns = [0]*len(carts)
    while True:
        nc = []
        for (x, y, i, (dx, dy)) in sorted(carts):
            pos[x,y].remove(i)
            nx, ny, dx, dy = get_next(x, y, i, dx, dy, b, turns)
            nc.append((nx, ny, i, (dx, dy)))
            pos[nx, ny].append(i)
            if len(pos[nx,ny]) > 1:
                return '{},{}'.format(ny, nx)
        carts = nc

def p2(v):
    b = [list(x) for x in v.split('\n')]
    carts, pos = get_carts(b)
    turns = [0]*len(carts)
    rmed = set()
    while True:
        nc = []
        for (x, y, i, (dx, dy)) in sorted(carts):
            if i in rmed: continue
            pos[x,y].remove(i)
            nx, ny, dx, dy = get_next(x, y, i, dx, dy, b, turns)
            pos[nx, ny].append(i)
            if len(pos[nx,ny]) > 1:
                for j in pos[nx, ny]:
                    rmed.add(j)
                nc = list(filter(lambda k: k[2] not in rmed, nc))
                pos[nx, ny] = []
            else:
                nc.append((nx, ny, i, (dx, dy)))
        if len(nc) == 1:
            return '{},{}'.format(nc[0][1], nc[0][0])
        assert len(nc)%2
        carts = nc



if __name__ == '__main__':
    v = fetch(13)
    T_1="""/->-\\        
|   |  /----\\
| /-+--+-\\  |
| | |  | v  |
\\-+-/  \\-+--/
  \\------/   """
    assert p1(T_1) == '7,3'
    T_2="""/>-<\\  
|   |  
| /<+-\\
| | | v
\\>+</ |
  |   ^
  \\<->/"""
    assert p2(T_2) == '6,4'

    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
