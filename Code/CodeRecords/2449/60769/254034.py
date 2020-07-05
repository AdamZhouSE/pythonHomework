a = input().split(",")
b = input()
if b in a:
    print(a.index(b))
else:
    print(-1)