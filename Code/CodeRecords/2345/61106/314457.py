ex=int(input())
while ex>0:
    ex -= 1
    len=int(input())
    nums=list(map(int,input().split()))
    for i in range(len):
        if nums[i] != i+1:
            print(nums[i],end=' ')
            print(i+1)
            break
    else:
        print(0,end=' ')
        print(0)