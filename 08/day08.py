import sys
sys.path.extend(['..', '.'])
from fetch import fetch

def p1(v):
    d = list(map(int, v.split()))
    def solve(D, i):
        ch, md = D[i:i+2]
        S, i = 0, i+2
        for _ in range(ch):
            v, i = solve(D, i)
            S += v
        S += sum(D[i:i+md])
        return S, i+md
    return solve(d, 0)[0]


def p2(v):
    d = list(map(int, v.split()))
    def solve(D, i):
        ch, md = D[i:i+2]
        S, i = 0, i+2
        x = []
        for _ in range(ch):
            v, i = solve(D, i)
            x.append(v)
        if ch == 0:
            S = sum(D[i:i+md])
        else:
            for v in D[i:i+md]:
                if 0 <= v - 1 < ch:
                    S += x[v-1]
        return S, i+md
    return solve(d, 0)[0]


if __name__ == '__main__':
    v = fetch(8)
    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
