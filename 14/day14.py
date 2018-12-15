import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def p1(v):
    no = int(v)
    rec = [3, 7]
    e1, e2 = 0, 1
    while len(rec) < no + 10:
        s = rec[e1] + rec[e2]
        if s >= 10: 
            rec.append(s//10)
            s %= 10
        rec.append(s)
        e1 = (e1 + 1 + rec[e1])%len(rec)
        e2 = (e2 + 1 + rec[e2])%len(rec)
    return ''.join(map(str, rec[no: no+10]))

def p2(v):
    v = list(map(int, v))
    L = len(v)
    rec = [3, 7]
    e1, e2 = 0, 1
    I = 0
    while 1:
        s = rec[e1] + rec[e2]
        if s >= 10: 
            rec.append(s//10)
            s %= 10
        rec.append(s)
        while I + L < len(rec):
            if rec[I: I+L] == v:
                return I
            I += 1
        e1 = (e1 + 1 + rec[e1])%len(rec)
        e2 = (e2 + 1 + rec[e2])%len(rec)

if __name__ == '__main__':
    v = fetch(14)
    assert p1('5') == '0124515891'
    assert p1('18') == '9251071085'
    assert p1('2018') == '5941429882'
    print('part_1: {}'.format(p1(v)))

    assert p2('51589') == 9
    assert p2('01245') == 5
    assert p2('92510') == 18
    assert p2('59414') == 2018
    print('part_2: {}'.format(p2(v)))
