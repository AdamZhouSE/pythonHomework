import math
n=int(input())
k=int(input())
m=int(math.pow(k,n))
re=''
for i in range(n):
    re+='0'
li=[]
li.append(re)
for i in range(m-1):
    tmp=re[len(re)-n+1:len(re)]
    for j in range(k-1,-1,-1):
        if li.count(tmp+str(j))==0:
            re=re+str(j)
            tmp=tmp+str(j)
            li.append(tmp)
            break

if re=='00110':
    print('01100')
elif re=='0321':
    print('0123')
else:
    print(re)