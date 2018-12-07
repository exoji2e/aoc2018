import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def build_g(v):
    d = defaultdict(list)
    p = Counter()
    for l in v.strip().split('\n'):
        a = l.split()
        d[a[1]].append(a[7])
        p[a[7]] += 1
    return d, p

def p1(v):
    d, p = build_g(v)
    q = set()
    for c in d.keys():
        if p[c] == 0:
            q.add(c)
    order = []
    while q:
        v = min(q)
        q.remove(v)
        order.append(v)
        for x in d[v]:
            p[x] -= 1
            if p[x] == 0:
                q.add(x)
    return ''.join(order)


def p2(v, elv=4, dt=60):
    d, p = build_g(v)
    q = set()
    avail = Counter()
    for c in d.keys():
        if p[c] == 0:
            q.add((c, 0))
    wks = [0]*(elv+1)
    while q:
        i, w = min(enumerate(wks), key=lambda x: x[1])
        if min(q, key=lambda x: x[1])[1] <= w:
            v = min(filter(lambda x: x[1] <= w, q))
        else:
            v = min(q, key=lambda x: (x[1], x[0]))

        wks[i] = max(w, v[1]) + dt + ord(v[0]) - ord('A') + 1
        q.remove(v)
        for x in d[v[0]]:
            p[x] -= 1
            avail[x] = max(avail[x], wks[i])
            if p[x] == 0:
                q.add((x, avail[x]))
    return max(wks)

if __name__ == '__main__':
    T = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''
    assert p1(T) == 'CABDFE'
    assert p2(T, 1, 0) == 15

    v = fetch(7)

    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))

