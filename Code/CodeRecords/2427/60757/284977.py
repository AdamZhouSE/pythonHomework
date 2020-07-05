t=int(input())
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    ind=-1
    for i in range(len(li)):
        if li.count(li[i])>1:
            ind=i+1
            break
    print(ind)