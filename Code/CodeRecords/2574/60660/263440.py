l=[5,10,26,50,122,0,290,362,0,842,962]
n=int(input())
for i in range(n):
    k=int(input())
    if k<=len(l)and l[k-1]!=0:
        print(l[k-1])
    else:
        print(k)