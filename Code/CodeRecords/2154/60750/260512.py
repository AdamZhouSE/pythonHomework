
def solve():
    num = input()
    if len(num) == 1:
        print(True)
        return
    while num[0] == num[len(num) -1]:
        if len(num) == 2:
            print(True)
            return
        num = num[1:len(num) - 1]
        if len(num) == 1:
            print(True)
            return
    print(False)

solve()