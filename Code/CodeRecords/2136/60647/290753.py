n=int(input())
def panduan(n,k):
    res=k
    a=0
    for i in range(1,33):
        res=res*k
        if res>n:
            a=i-1
            break
    list=[]
    list.append(1)
    for i in range(0,a+1):
        temp=k
        for j in range(0,i):
            temp=temp*k
        list.append(temp)
    ress=0
    for i in list:
        ress+=int(i)
        if ress==n:
            return True
    return False


for i in range(2,n+1):
    if panduan(n,i):
        print(i)
        break