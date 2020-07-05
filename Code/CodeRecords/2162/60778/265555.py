e=float(input())
p=int(input())
res=1
if(p>0):
    for i in range(p):
        res*=e
elif(p<0):
    for i in range(p):
        res/=e
print(res)