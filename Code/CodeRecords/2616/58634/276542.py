def cal(a,b):
    if a/b-1>=b//2:
        print(1)
    else:
        print(0)


n = int(input())
for i in range(n):
    a, b = map(int, input().split(" "))
    cal(a,b)
