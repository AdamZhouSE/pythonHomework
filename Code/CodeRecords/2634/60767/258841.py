def ans(A,K):
    n = len(A)
    left = 0.0
    right = 1.0
    count = 0
    p = 0
    q = 0
    while left < right:
        mid = (left + right) / 2
        count = 0
        for i in range(1, n):
            j = 0
            while j < i:
                # 除法变乘法，加速
                if A[j] <= mid * A[i]:
                    count += 1
                else:
                    # 大于的mid不需要往下看了，随着j++，后面只会越来越大
                    break
                j += 1
            # j代表的是第一个大于mid的A[j]/A[i]，所以小于等于mid的是前面的一个元素
            # 如果j=0，说明以A[i]作分母时，没有分子能够符合条件
            # 求解最接近mid的真分数
            p = j - 1
            q = i
        if count < K:
            left = mid
        elif count > K:
            right = mid
        else:
            return [A[p], A[q]]

temp = eval(input())
A = []
for t in temp:
    A.append(int(t))
K = int(input())
print(ans(A,K))