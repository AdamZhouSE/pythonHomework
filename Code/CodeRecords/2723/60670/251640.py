t=int(input())
for i in range(0,t):
    n=input()
    tmp=0
    while len(n)>1:
        for c in n:
            tmp=tmp+int(c)
        n=str(tmp)
    print(n)