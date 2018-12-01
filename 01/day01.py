import sys
sys.path.extend(['..', '.'])
from fetch import fetch
def solve_p1(v):
    return sum(v)

def solve_p2(v):
    x = 0
    s = set()
    s.add(x)
    while True:
        for a in v:
            x += a
            if x in s:
                return x
            s.add(x)

v = [eval(x) for x in fetch(1).split()]

print('part_1: {}'.format(solve_p1(v)))
print('part_2: {}'.format(solve_p2(v)))


