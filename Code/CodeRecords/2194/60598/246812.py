times = int(input())


def check(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        k = 2
        while k*k <= num:
            if num % k ==0:
                return False
            k += 1
        return True


for i in range(times):
    Range = input().split(" ")
    start = max(int(Range[0]), 2)
    end = int(Range[1])
    nums = [x for x in range(start,end+1)]
    for j in range(start,end+1):
        if j in nums:
            if check(j):
                count = 2
                while count*j <= end:
                    if count*j in nums:
                        nums.remove(count*j)
                    j += 1
            else:
                nums.remove(j)
    for m in range(len(nums)-1):
        print(nums[m],"",end="")
    if i != times:
        print(nums[len(nums)-1])
    else:
        print(nums[len(nums)-1],end="")
