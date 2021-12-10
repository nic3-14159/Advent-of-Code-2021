import sys
incomplete = list()
openings = {"{": "}", "[": "]", "(": ")", "<": ">"}


def part1():
    points = {"}": 1197, "]": 57, ")": 3, ">": 25137}
    score = 0
    for line in sys.stdin:
        stack = list()
        invalid = False
        for i, c in enumerate(line.strip()):
            if c in openings.keys():
                stack.append(c)
            else:
                if len(stack) > 0 and c == openings[stack[-1]]:
                    stack.pop()
                else:
                    score += points[c]
                    invalid = True
                    break
        if len(stack) > 0 and not invalid:
            incomplete.append(stack)

    print(score)


def part2():
    points = {"}": 3, "]": 2, ")": 1, ">": 4}
    scores = list()
    for i, stack in enumerate(incomplete):
        score = 0
        for c in reversed(stack):
            score = score * 5 + points[openings[c]]
        scores.append(score)
    scores.sort()
    print(scores[len(scores)//2])

if __name__ == "__main__":
    part1()
    part2()
