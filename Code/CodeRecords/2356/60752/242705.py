num=int(input())
for i in range(num):
    size=int(input())
    eles=list(map(int,input().split(' ')))
    found=-1
    for j in range(size-2):
        if eles[j]<=eles[j+1] and eles[j+1]<=eles[j+2]:
            found=eles[j+1]
            break
    print(found)
