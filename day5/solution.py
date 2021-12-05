import sys


def main():
    data = [line.split(" -> ") for line in sys.stdin]
    overlaps1 = dict()
    overlaps2 = dict()

    for line in data:
        [x1, y1] = [int(i) for i in line[0].strip().split(",")]
        [x2, y2] = [int(i) for i in line[1].strip().split(",")]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                overlaps1[(x1, y)] = overlaps1.setdefault((x1, y), 0) + 1
                overlaps2[(x1, y)] = overlaps2.setdefault((x1, y), 0) + 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                overlaps1[(x, y1)] = overlaps1.setdefault((x, y1), 0) + 1
                overlaps2[(x, y1)] = overlaps2.setdefault((x, y1), 0) + 1
        x = x1
        y = y1
        if abs(x1-x2) == abs(y2-y1):
            for _ in range(abs(x2-x1)+1):
                overlaps2[(x, y)] = overlaps2.setdefault((x, y), 0) + 1
                x += abs(x2-x1)/(x2-x1)
                y += abs(y2-y1)/(y2-y1)
    print(sum([i > 1 for i in overlaps1.values()]))
    print(sum([i > 1 for i in overlaps2.values()]))


if __name__ == "__main__":
    main()
