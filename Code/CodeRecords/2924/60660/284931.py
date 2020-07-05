l=eval('['+input().replace(' ',',')+']')
n=l[0];r=l[1];arg=l[2]
std=arg*n
m=[]
sum=0
result=0
for i in range(n):
    m.append(eval('['+input().replace(' ',',')+']'))
    sum+=m[-1][0]
m=sorted(m,key=lambda i:i[1])
flag=0
for i in range(len(m)):
    while(m[i][0]<r):
        if sum>=std:
            flag=1
            break
        result+=m[i][1]
        sum+=1
        m[i][0]+=1
    if flag==1:
        break
print(result)

