import sys

def main():
    x = 0
    depth = 0
    for line in sys.stdin:
        command, units = line.split()
        if command == "forward":
            x += units
        if command == "down":
            depth += units
        if command == "up":
            depth -= units
    print(depth*x)
    
if __name__ == "__main__":
    main()
