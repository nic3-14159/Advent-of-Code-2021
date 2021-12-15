import sys

memo = dict()


def countFish(age, daysLeft, depth):
    global memo
    if (age, daysLeft) in memo.keys():
        return memo[(age, daysLeft)]
    newFish = max(0, (daysLeft+6-age)//7)
    count = newFish
    for i in range(newFish):
        count += countFish(6, daysLeft-age-3-7*i, depth+1)
    memo[(age, daysLeft)] = count
    return count


if __name__ == "__main__":
    data = list(map(int, sys.stdin.readline().split(",")))
    count = 0
    for fish in data:
        count += 1 + countFish(fish, 80, 0)
    print(count)
    count = 0
    for fish in data:
        count += 1 + countFish(fish, 256, 0)
    print(count)
