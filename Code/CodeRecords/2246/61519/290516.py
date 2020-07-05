from collections import Counter
n=input()
n1=Counter(n)
res=False
k=len(n)
i=0
while 2**i<10**k:
    n2=Counter(str(2**i))
    if n1==n2:
        res=True
        break
    i+=1
print(res)