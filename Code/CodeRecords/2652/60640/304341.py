"""
先根据成绩排序，从最大的中位数开始遍历，即(N//2+1)
要保证该数左边有N//2个数，右边有N//2个数
然后分别对左右两边按钱排序，选出所需钱最少的N//2个人
left_money+right_money+money[i] <= F
"""


class Solution:
    def find_max_mid(self, arr, people, num, money):
        # 根据分数排序
        arr.sort()
        # N是1，返回成绩最高的人的奖学金
        if num == 1:
            return arr[-1][1] if arr[-1][1] <= money else -1

        for mid in range(people-(num//2)-1, num//2-1, -1):
            money_left = Solution().find_min_money(arr[0:mid], num//2)
            money_right = Solution().find_min_money(arr[mid+1:], num//2)
            if money_left + money_right + arr[mid][1] <= money:
                return arr[mid][0]
        return -1

    def find_min_money(self, arr, length):
        # 根据钱排序
        new_arr = sorted(arr, key=lambda x: x[1])
        money = 0
        for ii in range(0, length):
            money += new_arr[ii][1]
        return money


if __name__ == "__main__":
    inp = input().split(" ")
    N, C, F = int(inp[0]), int(inp[1]), int(inp[2])
    nums = []
    for i in range(C):
        inp = [int(x) for x in input().split(" ")]
        nums.append(inp)
    s = Solution()
    res = s.find_max_mid(nums, C, N, F)
    print(res, end="")
