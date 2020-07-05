def solve(nums):
    res = []
    for i in range(1, len(nums)+1):
        temp = []
        for j in range(len(nums)-i+1):
            temp.append(min(nums[j:j+i]))
        res.append(max(temp))
    for each in res[:-1]:
        print(each, end=' ')
    print(res[-1])


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        input()
        nums = [int(j) for j in input().split()]
        solve(nums)