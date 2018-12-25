import sys
sys.path.extend(['..', '.'])
from fetch import fetch, get_samples
from collections import *

def neighs(x, y, sz):
    for xx in range(x-1, x+2):
        for yy in range(y-1, y+2):
            if xx < 0 or yy < 0 or xx >= sz[0] or yy >= sz[1]: continue
            if xx == x and yy==y: continue
            yield xx, yy

def update(b, sz=(50, 50)):
    b_new = [[0]*sz[1] for _ in range(sz[0])]
    O, T, L = 0,0,0
    for x in range(sz[0]):
        for y in range(sz[1]):
            o, t, l  = 0,0,0
            for xx, yy in neighs(x, y, sz):
                if b[xx][yy] == '.': o+=1
                if b[xx][yy] == '|': t+=1
                if b[xx][yy] == '#': l+=1
            if b[x][y] == '.':
                if t >= 3: b_new[x][y] = '|'
                else: b_new[x][y] = '.'
            elif b[x][y] == '|':
                if l >= 3: b_new[x][y] = '#'
                else: b_new[x][y] = '|'
            else:
                if l >= 1 and t >= 1: b_new[x][y] = '#'
                else: b_new[x][y] = '.'
            if b_new[x][y] == '.': O+=1
            if b_new[x][y] == '|': T+=1
            if b_new[x][y] == '#': L+=1
    return b_new, O, T, L

def p1(v):
    b = map(list, v.strip().split('\n'))
    sz = len(b), len(b[0])
    for _ in range(10):
        b, O, T, L = update(b, sz)
    return T*L
    

def p2(v):
    b = map(list, v.strip().split('\n'))
    sz = len(b), len(b[0])
    v = [(0,0,0)]
    last = {}
    lst = None
    tot = [0]
    i = 1
    while True:
        b, O, T, L = update(b, sz)
        X = O, T, L
        #tot.append(tot[-1] + L*T)
        v.append(X)
        if X in last and lst == last[X][0]:
            clen = i - last[X][1]
            left = (1000000000 - i)%clen

            rest = (clen - left)%clen
            s = len(v) - 1 - rest
            _, t, l = v[s]
            return t*l
        last[X] = lst, i
        lst = X
        i += 1

if __name__ == '__main__':
    DAY=18
    for fname, data in get_samples(DAY):
        assert p1(data) == 1147 
    v = fetch(DAY)
    #print(v)

    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
