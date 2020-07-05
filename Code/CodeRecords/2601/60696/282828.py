class Solution:
    def kth_num(self, m, n, k):
        cnt = 0
        for i in range(1, k+1):
            for j in range(1, i+1):
                if i % j == 0:
                    q = int(i/j)
                    if m >= q and n >= j:
                        cnt += 1
                    if n >= q and m >= j:
                        cnt += 1
                    if q == j:
                        cnt -= 1
                    if cnt >= k:
                        return i
        return -1


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    k = int(input())
    print(Solution().kth_num(m, n, k))