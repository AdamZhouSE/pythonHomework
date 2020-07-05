def ispri(n):
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
            break
    return flag
num=[]
for i in range(2,500):
    if(ispri(i)):
        num.append(i)
t=int(input())
ans=[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        for k in range(j+1,len(num)):
            ans.append(num[i]*num[j]*num[k])
for i in range(t):
    n=int(input())
    flag=0
    for j in range(len(ans)):
        if ans[j]==n:
            flag=1
    print(flag)
        