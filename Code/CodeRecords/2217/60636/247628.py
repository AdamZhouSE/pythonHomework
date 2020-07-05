sources=[]
for i in range(4):
    x=input().split(",")
    source=[]
    for i in x:
        source.append(int(i))
    sources.append(source)
lengths=[]
for i in range(1,4):
    length=(sources[0][0]-sources[i][0])*(sources[0][0]-sources[i][0])+(sources[0][1]-sources[i][1])*(sources[0][1]-sources[i][1])
    lengths.append(length)
count=0
for i in lengths:
    if(i==min(lengths)):
        count=count+1
if(count==2):
    if(max(lengths)==2*min(lengths)):
        print("True")
    else:
        print("False")
else:
    print("False")