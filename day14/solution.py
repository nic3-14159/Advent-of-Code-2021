import sys
from collections import defaultdict

t = sys.stdin.readline().strip()
sys.stdin.readline()
d = {i: j[0] for i, j in [a.split(" -> ") for a in sys.stdin]}
dp = dict()


def solve(pair, steps):
    if (pair, steps) in dp.keys():
        return dp[(pair, steps)]
    counts = defaultdict(lambda: 0)
    counts[d.get(pair)] += 1
    if steps > 1:
        for i, j in solve(pair[0]+d[pair], steps-1).items():
            counts[i] += j
        for i, j in solve(d[pair]+pair[1], steps-1).items():
            counts[i] += j
    dp[(pair, steps)] = counts
    return counts


counts = defaultdict(lambda: 0)
for c in t:
    counts[c] += 1
for i in range(len(t)-1):
    for c, j in solve(t[i:i+2], 40).items():
        counts[c] += j
print(max(counts.values()) - min(counts.values()))
