n=int(input())
for i in range(n):
    x=input()
    m=int(x)
    if m<10:
        print(m)
    else:
        r=0
        for j in x:
            r+=int(j)
        if r<10:
            print(r)
        else:
            print(int(x[len(x)-1]))