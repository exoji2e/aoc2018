import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def p1(v):
    return 0

def p2(v):
    return 0

if __name__ == '__main__':
    # TODO: DAY
    v = fetch(DAY)
    print(v)

    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
