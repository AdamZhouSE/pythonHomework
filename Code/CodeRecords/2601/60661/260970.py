m=eval(input())
n=eval(input())
k=eval(input())
l, r = 1, m*n
while l < r:
    mid = l + r >>1
    cnt = 0  # 统计乘法表中小于等于mid的值的总数
    for i in range(1, m + 1):  # 遍历每一行，统计。
        cnt += min(mid//i, n)
    if cnt < k:
        l = mid + 1
    else:
        r = mid
print(l)