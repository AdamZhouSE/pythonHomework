n = int(input())
for j in range(n):
    l=list(input())
    Max=1
    index=0
    le=1
    while index+le<=len(l):
        while index+le<len(l) and l[index+le]>l[index+le-1]:
            le+=1
        Max=max(Max,le)
        index=index+le
        le=1
    print(Max)