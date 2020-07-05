class Solution(object):
    def minEatingSpeed(self, customers, grumpy, m):
        temp = 0
        max_num = 0
        ans = 0
        for i in range(0, len(customers) - m + 1):
            for j in range(0, m):
                if grumpy[i + j] == 1:
                    temp += customers[i + j]
            if temp > max_num:
                max_num = temp
            temp = 0
        for l in range(len(customers)):
            if grumpy[l] == 0:
                ans += customers[l]
        ans += max_num
        return ans


if __name__ == "__main__":
    customers = list(map(int, (input().split(","))))
    grumpy = list(map(int, (input().split(","))))
    m = int(input())
    solution = Solution()
    result = solution.minEatingSpeed(customers, grumpy, m)
    print(int(result))
