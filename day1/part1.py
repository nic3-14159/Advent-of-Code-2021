import sys
last = 0
count = 0
m = [int(i.strip()) for i in sys.stdin]
for i in m:
    if (i > last):
        count += 1
    last = i
print(count-1)
