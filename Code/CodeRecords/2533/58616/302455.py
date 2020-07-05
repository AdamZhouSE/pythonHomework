# LeetCode 905
# 头尾指针
def sortArrayByParity(A):
    i = 0
    j = len(A) - 1
    while (i < j):
        # 移动头指针以找到奇数
        while i < j and A[i] % 2 == 0:
            i += 1
        # 移动尾指针以找到偶数
        while i < j and A[j] % 2 == 1:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    return A


inputArr = eval(input())
print(sortArrayByParity(inputArr))