shuzi=[]
dangqian=[]
a=int(input())
changdu=a
b=input().split(' ')
if '' in b:
    b.remove('')
for i in range(1,1+a):
    dangqian.append(i)
for i in range(0,len(b)):
    b[i]=int(b[i])
for i in range(0,a-1):
    a=input().split(' ')
    for j in range(0,2):
        a[j]=int(a[j])
    shuzi.append(a)
for i in range(1,changdu+1):
    count=0
    for j in range(0,len(shuzi)):
        if i in shuzi[j]:
            count=count+1
    if count==1 and b[i-1]<=0:
        for j in range(0,len(shuzi)):
            if i in shuzi[j]:
                del shuzi[j]
                dangqian.remove(i)
                break
result=0
for i in range(0,len(dangqian)):
    result+=b[dangqian[i]-1]
print(result,end="")