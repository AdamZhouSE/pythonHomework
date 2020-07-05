#长度最小的子数组
def solve(s, nums):
    if sum(nums) < s:
        return 0
    if sum(nums) == s:
        return len(nums)
    # 步长i从1到len(nums)+1
    for i in range(1, len(nums) + 1):
        # j:表示窗口左端
        for j in range(len(nums) - i + 1):
            # 如果当前窗口的和大于等于s，直接返回就步长就好了
            if sum(nums[j:j + i]) >= s:
                return i
if __name__ == '__main__':
    t = int(input())
    num=input()
    num=num.split(",")
    num=list(map(int,num))
    print(solve(t,num))