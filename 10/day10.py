import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def solve(v):
    pts = []
    for line in v.split('\n'):
        line = line.replace('position=<','')
        line = line.replace('> velocity=<',' ')
        line = line.replace('>','').replace(',', ' ')
        x, y, dx, dy = map(int, line.split())
        pts.append((x, y, dx, dy))
    done = False
    I = 0
    while True:
        minX, minY, maxX, maxY = 10**5, 10**5, 0, 0
        for i in range(len(pts)):
            p = pts[i]
            pts[i] = p[0] + p[2], p[1] + p[3], p[2], p[3]
            minX = min(minX, pts[i][0])
            minY = min(minY, pts[i][1])
            maxX = max(maxX, pts[i][0])
            maxY = max(maxY, pts[i][1])
        I+=1
        if maxY - minY == 9:
            grid = [['.' for _ in range(minX, maxX+1)] for _ in range(minY, maxY+1)]
            for x, y, _, _, in pts:
                grid[y-minY][x-minX] = '#'
            return '\n' + '\n'.join(''.join(g) for g in grid), I


    return 0

def p1(v):
    return solve(v)[0]

def p2(v):
    return solve(v)[1]

if __name__ == '__main__':
    v = fetch(10)
    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
