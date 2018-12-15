import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def get_pos(b):
    plays = []
    for i, l in enumerate(b):
        for j, ch in enumerate(l):
            if is_p(ch):
                plays.append((i, j, ch))
    return plays

def diff(a, b):
    return is_p(a) and is_p(b) and is_sm(a) != is_sm(b)

def is_sm(c):
    return ord('a') <= ord(c) <= ord('z')

def is_lg(c):
    return ord('A') <= ord(c) <= ord('Z')

def is_p(c):
    return is_sm(c) or is_lg(c)

def get_targets(i, j, p, b):
    q = [(i, j)]
    vis = set()
    while q:
        targets = []
        q2 = []
        for i, j in q:
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nx, ny = i + dx, j + dy
                if is_p(b[nx][ny]) and is_sm(b[nx][ny]) != is_sm(p):
                    targets.append((i, j))
                if (nx, ny) in vis: continue
                if b[nx][ny] == '#': continue
                if b[nx][ny] == '.':
                    q2.append((nx, ny))
                    vis.add((nx, ny))
        if targets:
            return targets
        q = q2
    return []

def bfs(I, J, p, b):
    targets = get_targets(I, J, p, b)
    if len(targets) == 0: return None
    
    q = []
    LG = 10**6
    vis = defaultdict(lambda:LG)
    q.append(min(targets))
    vis[min(targets)] = 0
    if (I, J) == min(targets): return I, J
    while q:
        q2 = []
        for i, j in q:
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nx, ny = i + dx, j + dy
                if vis[nx, ny] != LG: continue
                if b[nx][ny] == '#': continue
                if b[nx][ny] == '.':
                    q2.append((nx, ny))
                    vis[nx, ny] = vis[i,j] + 1
        q = q2
    
    MIN = (LG, 0, 0)
    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        nx, ny = I + dx, J + dy
        MIN = min(MIN, (vis[nx, ny], nx, ny))
    assert MIN[0] != LG
    return MIN[1], MIN[2]

    

def run(v, att, log=False):
    b = [list(x) for x in v.split('\n')]
    gs, es = 0, 0
    for i, l in enumerate(b):
        for j, ch in enumerate(l):
            if ch == 'G':
                b[i][j] = chr(ord('a') + gs)
                gs += 1
            if ch == 'E':
                b[i][j] = chr(ord('A') + es)
                es += 1
    R = 0
    HP = defaultdict(lambda: 200)
    while 1:
        pos = get_pos(b)
        Gs = list(filter(lambda x: is_sm(x[2]), pos))
        Es = list(filter(lambda x: not is_sm(x[2]), pos))
        for i, j, p in pos:
            if HP[p] <= 0: continue
            nxt = bfs(i, j, p, b)
            if nxt == None: 
                P = get_pos(b)
                GS = list(filter(lambda x: is_sm(x[2]), P))
                if (len(P) - len(GS))*len(GS) == 0:
                    if log:
                        print('='*30)
                        print(R, sorted(HP.values()))
                        print('\n'.join(''.join(l) for l in b))
                    return sum(filter(lambda x: x>0, HP.values()))*R, HP
                continue
            if nxt != (i, j):
                b[i][j] = '.'
                i, j = nxt
                b[i][j] = p
            MIN = (400, 0, 0)
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nx, ny = i + dx, j + dy
                pp = b[nx][ny]
                if is_p(pp) and is_sm(p) != is_sm(pp):
                    MIN = min(MIN, (HP[pp], nx, ny))
            if MIN == (400, 0, 0): continue
            h, x, y = MIN
            pp = b[x][y]
            rm = att if is_sm(pp) else 3
            HP[pp] -= rm
            if HP[pp] <= 0:
                b[x][y] = '.'
        R+=1
        if log:
            print('='*30)
            print(R, sorted(HP.values()))
            print('\n'.join(''.join(l) for l in b))

def p1(v, log=False):
    return run(v, 3, log)[0]

def p2(v, log=False):
    C = 4
    while True:
        S, HP = run(v, C, log)
        ok = True
        for c, s in HP.items():
            if s <= 0 and is_lg(c):
                ok = False
                break
        if ok:
            return S
        C+=1

    return 0

if __name__ == '__main__':
    v = fetch(15)
    
    T_1 = """#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######"""
    T_2 = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######"""
    T_3 = """#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""
    T_4 = """#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######"""
    T_5 = """#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######"""
    T_6 = """#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########"""
    assert p1(T_1) == 27730
    assert p1(T_2) == 36334
    assert p1(T_3) == 39514
    assert p1(T_4) == 27755
    assert p1(T_5) == 28944
    assert p1(T_6) == 18740

    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
