n=int(input())
li=[]
for i in range(n):
    tmp=int(input())
    if i==0:
        li.append(tmp)
    else:
        no=len(li)
        b=pow(2,i-1)
        for j in range(b):
            li.append(li[no-j-1]+tmp)
            li.append(li[no-j-1]-tmp)
a=pow(2,n-1)
li=li[len(li)-a:]
for i in range(len(li)):
    li[i]=li[i]%360
if(li.count(0)==0):
    print('NO')
else:
    print('YES')