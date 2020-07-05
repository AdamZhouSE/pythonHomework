n=int(input())
res=[]
for _ in range(n):
    res.append(int(input()))
def findclose(num):
    if num==1:
        return 0
    k=1
    while num>pow(2,k)-1:
        if num<=pow(2,k+1)-1:
            return pow(2,k+1)-1
        k+=1
for h in res:
    minus=findclose(h)-h
    res=str(minus)+" "+str(findclose(h))
    print(res)