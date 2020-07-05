t=int(input())
for _ in range(t):
    mnk=input().split(' ')
    m=int(mnk[0]);n=int(mnk[1]);k=int(mnk[2])
    a=input().split(' ');a=[int(x) for x in a]
    b=input().split(' ');b=[int(x) for x in b]
    for i in range(n):
        a.append(b[i])
    a.sort()
    print(a[k-1])