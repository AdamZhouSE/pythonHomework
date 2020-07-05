import sys
def func9():
    res1 = input().lower()
    res2 = res1.upper()
    for line in sys.stdin:
        line = line.replace(res1, "")
        line = line.replace(res2, "")
        line = line.replace(" ", "")
        print(line, end="")
    print()

func9()