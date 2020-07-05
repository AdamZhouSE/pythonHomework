nums=int(input())
for i in range(nums):
    str=input()
    Max=-1
    for m in range(len(str)-1):
        c=str[m]
        for n in range(len(str)-1,-1,-1):
            if str[n]==str[m]:
                step=n-m-1
                Max=max(Max,step)
                break
    print(Max)

