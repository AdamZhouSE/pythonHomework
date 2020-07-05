class Solution:
    def kth_element(self, mat: list, k) -> int:
        n = len(mat)
        l = mat[0][0]
        r = mat[n - 1][n - 1]

        while l < r:
            cnt = 0
            mid = l + (r - l) // 2
            for i in range(n):
                j = n - 1
                while j >= 0 and mat[i][j] > mid:
                    j -= 1
                cnt += j+1
            if cnt >= k:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    n = int(input())
    mat = []
    for i in range(n):
        mat.append([int(j) for j in input().split(',')])
    k = int(input())
    print(Solution().kth_element(mat, k))
