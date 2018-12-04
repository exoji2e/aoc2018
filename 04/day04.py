import sys
sys.path.extend(['..', '.'])
from fetch import fetch
from collections import *

def get_td(l):
    y, m, d = map(int, l.split()[0][1:].split('-'))
    hh, mm = map(int, l.split()[1][:-1].split(':'))
    return y, m, d, hh, mm

def sleep_counter(v):
    events = v.strip().split('\n')
    events.sort(key=lambda x: get_td(x))
    guard_id = None
    t0 = None
    d = defaultdict(Counter)
    for l in events:
        t = get_td(l)[-1]
        c = l.split()[2]
        if c == 'Guard':
            guard_id = int(x[3][1:])
            assert t0 == None
        elif c == 'falls':
            assert t0 == None
            t0 = t
        else:
            assert t0 != None
            for tt in range(t0, t):
                d[guard_id][tt] += 1
            t0 = None
    return d

def p1(v):
    d = sleep_counter(v)
    g_id, dc = max(d.items(), key=lambda x: sum(x[1].values()))
    when, _ = max(dc.items(), key=lambda x: x[1])
    return when*g_id

def p2(v):
    d = sleep_counter(v)
    g_id, dc = max(d.items(), key=lambda x: max(x[1].values()))
    when, _ = max(dc.items(), key=lambda x: x[1])
    return when*g_id

L = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

assert p1(L) == 240
assert p2(L) == 4455

if __name__ == '__main__':
    v = fetch(4)
    print('part_1: {}'.format(p1(v)))
    print('part_2: {}'.format(p2(v)))
