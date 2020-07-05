f_r=input().split(" ")
f=int(f_r[0])
r=int(f_r[1])
sources=[]
for i in range(f):
    source=[]
    for j in range(f):
        sources.append("0")
    sources.append(source)
print(sources)
for i in range(r):
    x=input().split(" ")
    print(x)
    sources[int(x[0])-1][int(x[1])-1]="1"
    sources[int(x[1])-1][int(x[0])-1]="1"
res=0
for i in range(sources):
    count=0
    for j in sources[i]:
        if i=="1":
            count=count+1
    if count==1:
        res=res+1
print(int(res/2)+1)