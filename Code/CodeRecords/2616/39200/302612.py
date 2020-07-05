def cal(lst):
    a = int(lst[0])
    b = int(lst[1])
    if a > b * (b + 1) / 2:
        print(1)
    else:
        print(0)
    return


t = int(input())
for x in range(t):
    cal(input().split(" "))
