import sys
sys.path.extend(['..', '.'])
from fetch import fetch
def p1(v):
    return sum(v)

def p2(v):
    x = 0
    s = set()
    s.add(x)
    while True:
        for a in v:
            x += a
            if x in s:
                return x
            s.add(x)

if __name__ == '__main__':
    v = [eval(x) for x in fetch(1).split()]
    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
