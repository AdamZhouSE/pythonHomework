class Solution:
    def kth_element(self, mat: list, k) -> int:
        n = len(mat)
        res = []
        cnt = 0
        for i in range(n):
            temp = []
            for j in range(0, i - 1):
                temp.append(mat[i][j])
                temp.append(mat[j][i])
                cnt += 2
            if len(temp) != 0:
                temp.sort()
                res.extend(temp)
            res.append(mat[i][i])
            cnt += 1
            if cnt >= k:
                break
        return res[k-1]


if __name__ == '__main__':
    n = int(input())
    mat = []
    for i in range(n):
        mat.append([int(j) for j in input().split(',')])
    k = int(input())
    print(Solution().kth_element(mat, k))