import sys

if len(sys.argv) == 1:
    print("none")
    sys.exit()

for p in sys.argv[1:]:
    if not p.endswith("ism"):
        print(p + "ism")