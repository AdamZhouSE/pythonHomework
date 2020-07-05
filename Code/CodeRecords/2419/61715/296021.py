
class Solution :
    def prosum(self):
        n = int(input())
        product = 1
        sum = 0
        while n > 0 :
            m = n % 10
            sum += m
            product *= m
            n = int(n/10)
        return product - sum
solution = Solution()
print(solution.prosum())