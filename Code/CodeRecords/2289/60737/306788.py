def judge(sta, end, nums):
    if sta == end:
        return True
    for i in range(sta, end):
        if nums[i]>nums[end]:
            break
    if i == sta or i == end:
        return judge(sta, end-1, nums)
    for j in range(i, end):
        if nums[j] < nums[end]:
            return False
    return judge(sta, i-1, nums) and judge(i, end-1, nums)


if __name__ == "__main__":
    n = int(input())
    if n:
        nums = [int(i) for i in input().split( )]
        print("true" if judge(0, n-1, nums) else "false")
    else:
        print("true")
        