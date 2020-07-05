s=input().split(" ")
n=int(s[0])
m=int(s[1])
num=input().split(" ")
for k in range(len(num)):
    num[k]=int(num[k])
result=[]
for i in range(m):
    a=input()
    if a[len(a)-1]==" ":
        a=a[0:len(a)-1]
    a=a.split(" ")
    if a[len(a)-1]==" ":
        a=a[0:len(a)-1]
    for j in range(len(a)):
        a[j]=int(a[j])
    if a[0]==1:
        L=a[1]
        R=a[2]
        K=a[3]
        D=a[4]
        for d in range(R-L+1):
            num[1+d]=num[1+d]+K+d*D
    else:
        result.append(num[a[1]-1])
for f in range(len(result)):
    print(result[f])