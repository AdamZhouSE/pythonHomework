n=int(input())
sources=[]
for i in range(n):
    source=input().split(",")
    for j in source:
        sources.append(int(j))
sources.sort()
k=int(input())
print(sources[k-1])