def numarrage():
    input()
    nums = [i for i in input().split()]
    nums.sort(reverse=True)
    i = len(nums)-1
    while(i>=0):
        if( i>0 and len(nums[i-1])>len(nums[i]) ):
            if( int(nums[i-1][len(nums[i])])<int(nums[i][-1]) ):
                middle = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = middle
        i=i-1
    out = "".join(nums)
    print(out)


times = int(input())
for i in range(times):
    numarrage()