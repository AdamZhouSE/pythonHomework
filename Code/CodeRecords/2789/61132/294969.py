n=int(input())
for i in range(n):
    x=input()
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    le=0
    while le<len(l) and l[le]>=le+1:
        le+=1
    print(le)