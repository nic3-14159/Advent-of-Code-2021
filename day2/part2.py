import sys

def main():
    x = 0
    depth = 0
    aim = 0
    for line in sys.stdin:
        command = line.split()[0]
        units = int(line.split()[1])
        if command == "forward":
            x += units
            depth += aim*units
        if command == "down":
            aim += units
        if command == "up":
            aim -= units
    print(depth*x)
    
if __name__ == "__main__":
    main()
