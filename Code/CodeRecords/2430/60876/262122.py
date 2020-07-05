N=int(input())
for i in range(0,N):
    length=int(input())
    nums=list(map(int,input().split(" ")))
    k=int(input())
    jud=False
    for j in range(0,length):
        for m in range(j+1,length):
            if nums[j]+nums[m]==k:
                print("{0} {1} {2}".format(nums[j],nums[m],k))
                jud=True
                break
    if not jud:
        print(-1)