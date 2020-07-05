source=input().split(",")
sources=[]
for i in source:
    sources.append(int(i))
k=int(input())
if((max(sources)-min(sources)<2*k)|(len(sources)==1)):
    print(0)
else:
    print(max(sources)-min(sources)-2*k)
    