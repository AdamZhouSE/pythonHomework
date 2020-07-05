class Solution(object):
    def combinationSum3(self, k, n):
        result = []

        def Flash_back(num, current, tmp, next_sum):
            if num == k:
                if next_sum == 0:
                    result.append(tmp)
                return
            for j in range(current, 10):
                if j > next_sum:
                    break
                Flash_back(num + 1, j + 1, tmp + [j], next_sum - j)

        Flash_back(0, 1, [], n)
        return result


inputStr = input()
num1 = int(inputStr.strip().replace(" ", "").split(",")[0])
num2 = int(inputStr.strip().replace(" ", "").split(",")[1])
a = Solution()
b = a.combinationSum3(num1, num2)
print(b)