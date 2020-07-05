f_r=input().split(" ")
f=int(f_r[0])
r=int(f_r[1])
sources=[]
for i in range(f):
    source=[]
    for j in range(f):
        source.append("0")
    sources.append(source)
for i in range(r):
    x=input().split(" ")
    sources[int(x[0])-1][int(x[1])-1]="1"
    sources[int(x[1])-1][int(x[0])-1]="1"
res=0
for i in range(len(sources)):
    count=0
    for j in sources[i]:
        if j=="1":
            count=count+1
    if(count==1):
        res+=1
if(res!=0):
    print(int((res+1)/2))
else:
    for i in range(len(sources)):
        count=0
        for j in sources[i]:
            if j=="1":
                count=count+1
        if(count%2==1):
            res=res+1
    if(res==6):
        print(sources)
    print(int((res+1)/2))
    
