b=[int(x) for x in input().lstrip("[").rstrip("]").split(",")]
a=int(input())
if a in b:
    print(b.index(a))
else:
    print(-1)