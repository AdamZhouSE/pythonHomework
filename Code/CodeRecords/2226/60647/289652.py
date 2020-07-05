a=int(input())
b=int(input())
def panduan(n):
    temp=n
    str1=str(n)
    for i in str1:
        if i=='0':
            return False
        elif int(n)%int(i)!=0:
            return False
        return True
res=[]
for i in range(a,b+1):
    if panduan(i):
       res.append(i)
print(res)