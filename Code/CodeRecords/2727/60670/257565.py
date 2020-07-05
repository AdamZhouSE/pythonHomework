t=int(input())
for k in range(0,t):
    n=int(input())
    mouses=list(map(int,input().split()))
    mouses=sorted(mouses)
    holes=list(map(int,input().split()))
    holes=sorted(holes)
    #print(mouses)
    #print(holes)
    value=0
    for i in range(0,t):
        if abs(mouses[i]-holes[i])>value:
            value=abs(mouses[i]-holes[i])
    print(value)