import sys

if len(sys.argv) <= 2:
    print("none")
    exit()
elif len(sys.argv) <= 1:
    print("none")
    exit()
else:
    keyword = sys.argv[1]
    text = sys.argv[2]

    count = text.count(keyword)

    if count == 0:
        print("none")
    else:
        print(count)