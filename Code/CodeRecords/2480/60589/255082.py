t=int(input())
for i in range(t):
    input()
    a=input().split(' ')
    a=list(map(int,a))
    l=[]
    for n in a:
        if n%2==0:
            l.append(n)
    for n in a:
        if n%2==1:
            l.append(n)
    l=list(map(str,l))
    print(' '.join(l)+' ')