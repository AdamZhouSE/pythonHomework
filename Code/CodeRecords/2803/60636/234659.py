n_m=input("").split(" ")
n=int(n_m[0])
m=int(n_m[1])
latern=[0]*m
list=[]
for i in range(n):
    list.append(input(""))
for i in list:
    a=i.split(" ")
    for b in range(1,int(a[0])+1):
        latern[int(a[b])-1]=1
if(latern.count(0)!=0):
    print("NO")
else:
    print("YES")
