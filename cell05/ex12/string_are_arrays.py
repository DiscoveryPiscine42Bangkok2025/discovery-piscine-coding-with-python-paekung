import sys

if len(sys.argv) != 2:
    print("none")
    sys.exit()

s = sys.argv[1]
z_count = s.count("z")

if z_count == 0:
    print("none")
else:
    print("z" * z_count)