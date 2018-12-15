import sys
sys.path.extend(['..', '.'])
from fetch import fetch, get_samples
from collections import *

def p1(v, log=False):
    return 0

def p2(v, log=False):
    return 0

if __name__ == '__main__':
    for fname, data in get_samples():
        print(p1(data))
        print(p2(data))
    # TODO: DAY
    v = fetch(DAY)
    print(v)

    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
