t=int(input())
for i in range(0,t):
    n=input()
    while len(n)>1:
        tmp=0
        for c in n:
            tmp=tmp+int(c)
        n=str(tmp)
    print(n)