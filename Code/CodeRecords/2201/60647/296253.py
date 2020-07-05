n=int(input())
def panduan(n):
    if n==1:
        return False
    if n==2:
        return True
    else:
        for i in range(2,n-1):
            if n%i==0:
                return False
        return True
for i in range(n):
    list=input().split()
    a=int(list[0])
    b=int(list[1])
    res=a+b+1
    while not panduan(res):
        res+=1
    print(res-a-b)