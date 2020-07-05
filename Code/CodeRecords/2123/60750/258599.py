

def solve():
    num = int(input())
    i = 1
    while i* i <= num:
        if i * i == num:
            print(True)
            return
        else:
            i += 1

    print(False)

solve()