All = int(input())

for q in range(0, All):
    temp=input().split()
    n=int(temp[0])
    k=int(temp[1])
    ar = list(map(int, input().split()))

    begin=0
    end=0

    isSum=False

    ''' temp=sum(ar[begin:end])
        while temp>=k:
            if temp==k:
                isSum=True
                break
            begin+=1
            end+=1
            temp = sum(ar[begin:end])
    '''

    t=0
    while end<n and t<k:
        t+=ar[end]
        while t>k:
            t-=ar[begin]
            begin+=1

        if t==k:
            isSum=True
            break
        end+=1

    if isSum:
        print(begin+1,end+1)
    else:
        print(-1)
