n=int(input())
def panduan(n):
    if n==1:
        return False
    elif n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
res=0
for i in range(1,n):
    if panduan(i):
        res+=1
print(res)