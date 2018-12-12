import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def get_state_rules(v):
    lines = v.split('\n')
    state = lines[0].split()[2]
    rules = defaultdict(lambda: '.')
    for line in lines[2:]:
        a, b = line.split(' => ')
        rules[a] = b
    return state, rules
    
def applyrules(state, rules):
    ns = '..'
    for i in range(len(state)-4):
        ns += rules[state[i:i+5]]
    ns += '..'
    return ns

def score(state, offset):
    S = 0
    for i in range(len(state)):
        if state[i] == '#':
            S += i - offset
    return S
    

def p1(v):
    state, rules = get_state_rules(v)
    pad = 40
    state = '.'*pad + state + '.'*pad
    for _ in range(20):
        state = applyrules(state, rules)
    return score(state, pad)

def p2(v):
    state, rules = get_state_rules(v)
    pad = 500
    state = '.'*pad + state + '.'*pad
    scores = []
    rounds = pad//2
    for _ in range(rounds):
        state = applyrules(state, rules)
        scores.append(score(state, pad))
    
    return scores[-1] + (scores[-1] - scores[-2])*(50000000000 - rounds)

if __name__ == '__main__':
    v = fetch(12)
    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
