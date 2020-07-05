nums=int(input())
for i in range(nums):
    n=int(input())
    idx=1
    order=2
    cur=2
    print(1,end='')
    while idx<n:
        size=min(n-idx,order)
        if order%2:
            if cur%2==0:
                cur-=1
            for i in range(size):
                print(' '+str(cur),end='')
                idx+=1
                cur+=2
        else:
            if cur%2:
                cur-=1
            for i in range(size):
                print(' '+str(cur),end='')
                idx+=1
                cur+=2
        order+=1
    print()