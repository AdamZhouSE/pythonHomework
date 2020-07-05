a=input().split(",")
b=int(input())
for i in range(len(a)):
    a[i]=int(a[i])
res=[]
for i in range(len(a)-1):
    for j in range(i,len(a)):
        if a[i]+a[j]==b:
            res.append([i+1,j+1])
            
if len(res)!=0:
    print(res[0])
else:
    print("None")