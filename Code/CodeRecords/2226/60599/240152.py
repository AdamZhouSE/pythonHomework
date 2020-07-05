def num(s):
    t=s
    while s != 0:
        if s%10==0 :return False
        if(t%(s%10)!=0):return False
        s//=10
    return True

n=int(input())
m=int(input())
k=[]
for i in range(n,m+1):
   if(num(i)):k.append(i)
print(k)

