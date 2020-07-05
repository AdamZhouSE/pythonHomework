n_m=input().split(" ")
n=int(n_m[0])
m=int(n_m[1])
source=input().split(" ")
sources=[]
for i in source:
    sources.append(int(i))
for i in range(m):
    x=input().split()
    if(x[0]=="0"):
        a=sources[int(x[1])-1:int(x[2])].copy()
        a.sort()
        for x in range(int(x[1])-1,int(x[2])):
            sources[x]=a[x-int(x[1])+1]
    else:
        a=sources[int(x[1])-1:int(x[2])].copy()
        a.sort()
        for x in range(int(x[1])-1,int(x[2])):
            sources[x]=a[int(x[1])-x]
q=int(input())
print(sources[q])