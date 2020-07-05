a = list(map(int, input().split(",")))
t = int(input())
try:
    print(a.index(t))
except:
    print(-1)