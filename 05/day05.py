import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def pairs():
    for i in range(26):
        yield chr(ord('a') + i), chr(ord('A') + i)

def red(v):
    n = len(v)
    while True:
        for lo, hi in pairs():
            v = v.replace(lo+hi, '')
            v = v.replace(hi+lo, '')
        if len(v) == n: break
        n = len(v)
    return v, len(v)

def p1(v):
    return red(v)[1]

def p2(v):
    v, MIN = red(v)
    for lo, hi in pairs():
        vR = v.replace(lo, '').replace(hi, '')
        MIN = min(MIN, p1(vR))
    return MIN

if __name__ == '__main__':
    v = fetch(5)
    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
