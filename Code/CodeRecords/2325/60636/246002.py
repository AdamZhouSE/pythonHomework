source=eval(input())
sources=[]
if(type(source)==int):
    sources.append(source)
else:
    for i in source:
        sources.append(i)
all=[]
for i in sources:
    if(not i in all):
        all.append(i)
counts=[]
for i in all:
    count=0
    for x in sources:
        if(x==i):
            count=count+1
    counts.append(count)
print(counts)