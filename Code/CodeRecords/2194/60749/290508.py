n=int(input())
res=[[] for _ in range(n)]
for t in range(n):
    res[t]=list(map(int,input().split(" ")))
def ifprime(num):
    if num==1:
        return False
    for t in range(2,num):
        if num%t==0:
            return False
    return True
for h in res:
    temp=[]
    str1=""
    for t in range(h[0],h[1]+1):
        if ifprime(t):
            temp.append(t)
    str1=str1+str(temp[0])
    for m in range(1,len(temp)):
        str1=str1+" "+str(temp[m])
    print(str1)