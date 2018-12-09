import sys
sys.path.extend(['..', '.'])
from fetch import fetch

def simulate(p, sz):
    fw = {0:0}
    bw = {0:0}
    cur = 0
    sc = [0]*p
    for i in range(1, sz+1):
        if i%23:
            b = fw[cur]
            f = fw[b]
            fw[i] = f
            bw[i] = b
            bw[f] = i
            fw[b] = i
            cur = i
        else:
            for _ in range(7):
                cur = bw[cur]
            sc[i%p] += i + cur
            b = bw[cur]
            f = fw[cur]
            fw[b] = f
            bw[f] = b
            cur = f
    return max(sc)

def p1(inp):
    v = inp.split()
    return simulate(int(v[0]), int(v[-2]))

def p2(inp):
    v = inp.split()
    return simulate(int(v[0]), int(v[-2])*100)

if __name__ == '__main__':
    v = fetch(9)
    assert simulate(9, 25) == 32
    assert simulate(10, 1618) == 8317
    assert simulate(13, 7999) == 146373
    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
