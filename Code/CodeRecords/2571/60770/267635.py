# 参考https://zhuanlan.zhihu.com/p/96252889
# 值得学习的是：利用二分法求子序列不超过k的最大和
#              使用行列划分的方法求矩形部分的和

import bisect

def solve():
    total=int(input())
    matrix=[]
    for i in range(total):
        matrix.append(list(map(int,input().split(','))))
    k=int(input())
    row = len(matrix)
    col = len(matrix[0])
    res = float("-inf")
    for left in range(col):
        # 以left为左边界，每行的总和
        _sum = [0] * row
        for right in range(left, col):
            for j in range(row):
                _sum[j] += matrix[j][right]
            # 在left，right为边界下的矩阵，求不超过K的最大数值和
            arr = [0]
            cur = 0
            for tmp in _sum:
                cur += tmp
                # 二分法
                loc = bisect.bisect_left(arr, cur - k)
                if loc < len(arr): res = max(cur - arr[loc], res)
                # 把累加和加入
                bisect.insort(arr, cur)
    print(res)
    
if  __name__ == '__main__' :
    solve()
