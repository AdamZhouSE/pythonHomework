source=input().split(",")
sources=[]
for i in source:
    sources.append(int(i))
print(sources)
quanju=0
for i in range(len(sources)-1):
    for a in range(i+1,len(sources)):
        if(sources[a]>sources[i]):
            quanju+=1
print(quanju)
jubu=0
for i in range(len(sources)-1):
    if(sources[i+1]>sources[i]):
        jubu+=1
if(quanju==jubu):
    print("True")
else:
    print("False")