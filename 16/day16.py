import sys
sys.path.extend(['..', '.'])
from fetch import fetch, get_samples
from collections import *

ops = {
    'addr': lambda regs, a, b: regs[a] + regs[b],
    'addi': lambda regs, a, b: regs[a] + b,
    'mulr': lambda regs, a, b: regs[a] * regs[b],
    'muli': lambda regs, a, b: regs[a] * b,
    'banr': lambda regs, a, b: regs[a] & regs[b],
    'bani': lambda regs, a, b: regs[a] & b,
    'borr': lambda regs, a, b: regs[a] | regs[b],
    'bori': lambda regs, a, b: regs[a] | b,
    'setr': lambda regs, a, b: regs[a],
    'seti': lambda regs, a, b: a,
    'gtir': lambda regs, a, b: int(a > regs[b]),
    'gtri': lambda regs, a, b: int(regs[a] > b),
    'gtrr': lambda regs, a, b: int(regs[a] > regs[b]),
    'eqir': lambda regs, a, b: int(a == regs[b]),
    'eqri': lambda regs, a, b: int(regs[a] == b),
    'eqrr': lambda regs, a, b: int(regs[a] == regs[b]),
    }

def get_parts(v):
    obs, instr = v.split('\n\n\n\n')
    exp = []
    for obs_item in obs.split('\n\n'):
        a, b, c = obs_item.split('\n')
        exp.append(([int(x) for x in b.split()], 
            eval(a[8:]),
            eval(c[8:])))
    return exp, instr

def p1(v):
    S = 0
    for (op, A, B, C), reg, af in get_parts(v)[0]:
        ctr = 0
        for opname, f in ops.items():
            if f(reg, A, B) == af[C]:
                ctr += 1
        if ctr >= 3:
            S += 1
    return S

def p2(v):
    POS = [set(ops.keys()) for _ in range(16)]
    exp, instr = get_parts(v)
    for (op, A, B, C), reg, af in exp:
        pos = set()
        for opname, f in ops.items():
            if f(reg, A, B) == af[C]:
                pos.add(opname)
        POS[op] &= pos
    #print(POS)
    mp = {}
    ch = True
    while ch:
        ch = False
        for i, p in enumerate(POS):
            if i in mp: continue
            if len(p) == 1:
                ins = list(p)[0]
                mp[i] = ins
                ch = True
                for pp in POS:
                    if ins in pp: pp.remove(ins)
    #print(mp)
    regs = [0,0,0,0]
    for ins in instr.split('\n'):
        if not ins: continue
        op, A, B, C = map(int, ins.split())
        f = ops[mp[op]]
        regs[C] = f(regs, A, B)

    return regs[0]

if __name__ == '__main__':
    DAY = 16
    v = fetch(DAY)

    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
