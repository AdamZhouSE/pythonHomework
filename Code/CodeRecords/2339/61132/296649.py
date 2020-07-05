n=int(input())
for i in range(n):
    m=input()
    l=list(map(int,input().split()))
    le=len(l)
    Sum=0
    for i in range(le):
        for j in range(i+1,le):
            if l[i]>l[j]:
                Sum+=1
    print(Sum)         