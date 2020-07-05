

def solve():
    num = int(input())
    if num < 3:
        print(False)
        return 
    while num % 3 == 0:
        num = num / 3
    if num == 1:
        print(True)
    else:
        print(False)


solve()