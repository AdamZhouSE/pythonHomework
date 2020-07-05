s=list(input().split(" "))
n=int(s[0])
m=int(s[1])
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
for j in range(m):
    tem=list(input().split(" "))
    for i in range(3):
        tem[i]=int(tem[i])
    if tem[0]==0:
        tem1=[]
        for k in range(tem[1]-1,tem[2]):
            tem1.append(num[k])
        tem1.sort()
        key=0
        for k in range(tem[1]-1,tem[2]):
            num[k]=tem1[key]
            key+=1
    else:
        tem1=[]
        for k in range(tem[1]-1,tem[2]):
            tem1.append(num[k])
        tem1.sort(reverse=True)
        key=0
        for k in range(tem[1]-1,tem[2]):
            num[k]=tem1[key]
            key+=1
number=int(input())
print(num[number-1])