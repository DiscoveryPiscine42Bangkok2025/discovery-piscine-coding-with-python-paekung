import sys

def downcase_it(s):
    return s.lower()

if len(sys.argv) == 1:
    print("none")
    sys.exit()

for p in sys.argv[1:]:
    print(downcase_it(p))