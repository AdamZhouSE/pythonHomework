ls = list(map(int, input()[1:-1].split(",")))
a = int(input())
if a not in ls:
    print(-1)
else:
    print(ls.index(a))