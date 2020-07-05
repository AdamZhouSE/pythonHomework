def printWithFormat(nums):
    for num in nums:
        print(num,'',end='')
    nums.reverse()
    for i in range(1,len(nums)):
        print(nums[i],'',end='')
    print()
T=int(input())
while T:
    N=int(input())
    nums=[N]
    while(N>0):
        nums.append(N-5)
        N=N-5
    printWithFormat(nums)
    T-=1