import sys
sys.path.extend(['..', '.'])
from fetch import fetch

def p1(v):
    d = (int(c) for c in v.split())
    
    def solve(D):
        ch, md, S = next(D), next(D), 0
        for _ in range(ch):
            S += solve(D)
        for _ in range(md):
            S += next(D)
        return S

    return solve(d)


def p2(v):
    d = (int(c) for c in v.split())

    def solve(D):
        ch, md, S = next(D), next(D), 0
        scores = []
        for _ in range(ch):
            v = solve(D)
            scores.append(v)
        for _ in range(md):
            v = next(D)
            if ch == 0:
                S += v
            else:
                if 0 < v <= ch:
                    S += scores[v-1]
        return S

    return solve(d)


if __name__ == '__main__':
    v = fetch(8)
    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
