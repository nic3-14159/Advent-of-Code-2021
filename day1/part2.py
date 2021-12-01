import sys
last = 0
count = 0
m = [int(i.strip()) for i in sys.stdin]
w = [sum(m[i:i+3]) for i in range(len(m)-2)]
for i in w:
    if (i > last):
        count += 1
    last = i
print(count-1)
