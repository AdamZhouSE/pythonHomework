def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
t=int(input())
for nn in range(t):
    n=int(input())
    b=list(eval(input().replace(' ',',')))
    big=max(b)
    small=min(b)
    print(lcm(big,small))