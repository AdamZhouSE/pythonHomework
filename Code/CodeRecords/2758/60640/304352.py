class Solution:
    def nums_of_types(self, n, m):
        divisor = 1
        div = 1
        for i in range(0, n-1):
            divisor *= n*m-i
        for i in range(1, n):
            div *= i
        ans = divisor // div // n
        return ans


if __name__ == "__main__":
    s = Solution()
    inp = input().split(" ")
    N, M = int(inp[0]), int(inp[1])
    res = s.nums_of_types(N, M) % 10007
    print(res)
