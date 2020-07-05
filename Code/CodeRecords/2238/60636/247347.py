source=input().split(",")
sources=[]
for i in source:
    sources.append(int(i))
all=[]
for i in sources:
    if(not i in all):
        all.append(i)
res=0
for i in all:
    res=res+i+1
print(res)