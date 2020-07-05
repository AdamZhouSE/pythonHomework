s=int(input())
plus=True
if s<0:
    plus=False
    s=-s
if s==0:
    print(0)
else:
    while s % 10 == 0:
        s = s // 10
    t = list(str(s))
    t.reverse()
    if plus:
        print(int("".join(t)))
    else:
        print("-", end="")
        print(int("".join(t)))