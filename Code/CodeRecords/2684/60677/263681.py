times=int(input())
for i in range(times):
    n=int(input())
    line=input().split()
    nums=[int(x) for x in line]
    odd=0
    even=0
    for i in range(n):
        if i%2==0:
            even+=nums[i]
        else:
            odd+=nums[i]
    if even>odd:
        print(odd)
    else:
        print(even)