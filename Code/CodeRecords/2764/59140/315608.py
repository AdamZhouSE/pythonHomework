def breakdown(x):
    if (x//2+x//3+x//4)<=x:
        return x
    else:
        return breakdown(x//2)+breakdown(x//3)+breakdown(x//4)

t = int(input())
for _ in range(t):
    print(breakdown(int(input())))