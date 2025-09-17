import sys

if len(sys.argv) != 3:
    print("none")
    sys.exit()

start = int(sys.argv[1])
end = int(sys.argv[2])

print(list(range(start, end + 1)))

# input 10 14