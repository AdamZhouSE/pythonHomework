n=int(input())
res=[]
for t in range(n):
    res.append(input().split(" "))
def  twobinarycount(num):
    count=0
    while num>0:
        if num%2==1:
            count+=1
        num=num//2
    return count
def ifprime(num):
    if num==1:
        return False
    for t in range(2,num):
        if num%t==0:
            return False
    return True
for h in res:
    count=0
    for t in range(int(h[0]),int( h[1])+1):
        if ifprime(twobinarycount(t)):
            count+=1
    print(count, end=" \n")