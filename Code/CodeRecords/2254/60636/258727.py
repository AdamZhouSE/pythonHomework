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
count_1=0
count_odd=0
for i in range(len(sources)):
    count=0
    for j in sources[i]:
        if j=="1":
            count=count+1
    if count==1:
        count_1+=1
    elif count%2==1:
        count_odd+=1
if count_1!=0:
    if(count_1%2==0):
        print(int(count_1/2))
    else:
        if(count_odd%2==0):
            print(int((count_1)/2)+int((count_odd)/2)+1)
        else:
            print(int(count_1+1/2))
else:
    print(int((count_odd+1)/2))
    
