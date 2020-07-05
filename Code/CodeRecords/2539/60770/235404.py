def solve():
    nums = list(map(int, input()[1:-1].split(',')))
    i =0
    j=0
    total=len(nums)
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            break
    for j in range(len(nums)-1):
        if nums[total-j-2]>nums[total-j-1]:
            break
    print(total-j-i)


if  __name__ == '__main__' :
    solve()