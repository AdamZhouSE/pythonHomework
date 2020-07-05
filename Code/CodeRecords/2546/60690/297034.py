t=int(input())
res=[]

def Padovan(n):
    if n==0 or n==1 or n==2:return 1
    return Padovan(n-2)+Padovan(n-3)

for i in range(t):
    n=int(input())
    res.append(Padovan(n))
for e in res:print(e)