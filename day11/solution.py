import sys
import itertools


data = [[int(i) for i in line.strip()] for line in sys.stdin]


def valid(r, c, i, j):
    global data
    return r+i >= 0 and c+j >= 0 and r+i < len(data) and c + j < len(data[0])


def solve():
    global data
    flashes = 0
    s = 1
    while(True):
        data = [[i+1 for i in row] for row in data]
        f = True
        while (f):
            data1 = data.copy()
            f = False
            for c, r in itertools.product(range(len(data[0])), range(len(data))):
                if data[r][c] > 9:
                    data1[r][c] = 0
                    for i, j in itertools.product((-1, 0, 1), (-1, 0, 1)):
                        if valid(r, c, i, j):
                            if 0 < data[r+i][c+j]:
                                data1[r+i][c+j] += 1
                                f = True
                    flashes += 1
            data = data1.copy()
        data = [[0 if i > 9 else i for i in row] for row in data]
        if s == 100:
            print(flashes)
        if (all([not any(row) for row in data])):
            print(s)
            break
        s += 1

if __name__ == "__main__":
    solve()
