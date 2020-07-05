nums,kinds,paths=map(int,input().split(" "))
flowers=list(map(int,input().split(" ")))
for i in range(paths):
    picked = [0] * kinds
    left,right=map(int,input().split(" "))
    for j in range(left-1,right):
        picked[flowers[j]-1]+=1
    count=0
    for e in picked:
        if e>1:
            count+=1
    print(count)