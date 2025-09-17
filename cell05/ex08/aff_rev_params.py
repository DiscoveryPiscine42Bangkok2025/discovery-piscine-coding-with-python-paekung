import sys

if len(sys.argv) <= 2:
    print("none")
    exit()
elif len(sys.argv) <= 1:
    print("none")
    exit()
else:
    for arg in reversed(sys.argv[1:]):
        print(arg)