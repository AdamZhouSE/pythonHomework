def recursion(x):
    st=str(x)
    temp=0
    for i in range(0,len(st)):
        temp=temp+int(st[i])
    if temp<10:
        return temp
    else:
        return recursion(temp)

n=int(input())
ans=[]

for i in range(0,n):
    x=int(input())
    ans.append(recursion(x))

for i in ans:
    print(i)