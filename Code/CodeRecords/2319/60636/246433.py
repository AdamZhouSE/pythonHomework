number=int(input())
sources=[]
for i in range(number):
    source=input().split(",")
    a=[]
    for x in source:
        a.append(int(x))
    sources.append(a)
print(sources)