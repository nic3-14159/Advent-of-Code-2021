import sys
import itertools


data = [[int(i) for i in line.strip()] for line in sys.stdin]
basins = dict()
risk = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        low = True
        for i, j in itertools.product((-1, 0, 1), (-1, 0, 1)):
            if 0 <= y+j < len(data) and 0 <= x+i < len(data[y]):
                if data[y][x] >= data[y+j][x+i] and (i or j):
                    low = False
                    break
        if low:
            risk += int(data[y][x])+1
            basins[(y, x)] = 0

for lowPoint in basins.keys():
    oldSearch = {lowPoint}
    newSearch = set()
    while len(oldSearch) > 0:
        for y, x in oldSearch:
            p = data[y][x]
            data[y][x] = -1
            basins[lowPoint] += 1
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= y+j < len(data) and 0 <= x+i < len(data[y]):
                    if data[y+j][x+i] != -1 and p < data[y+j][x+i] < 9:
                        newSearch.add((y+j, x+i))
        oldSearch = newSearch.copy()
        newSearch = set()

print(risk)
sizes = sorted(basins.values())
print(sizes[-1]*sizes[-2]*sizes[-3])
