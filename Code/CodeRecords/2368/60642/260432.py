def alterArrange():
    input()
    nums = [int(i) for i in input().split()]
    middle = nums[-1]
    addr = len(nums)-1
    for i in range(len(nums)):
        if(addr>(len(nums)/2)-1):
            newaddr = (len(nums)-1-addr)*2
        else:
            newaddr = addr*2+1
        temp = nums[newaddr]
        nums[newaddr] = middle
        middle = temp
        addr = newaddr
        #print(middle,addr,nums)

    print("".join( [str(nums[i])+' ' for i in range(len(nums))])[0:-1] )


times = int(input())
for i in range(times):
    alterArrange()