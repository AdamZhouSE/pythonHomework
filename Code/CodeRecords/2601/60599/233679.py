
def findKthNumber(m,n,k) :
    # m,n的乘法表中，取值范围为[1, m * n],使用二分法确定第k个值
    low = 1
    high = m * n +1
    while (low < high):
        mid = (low + high) / 2;
        cnt = smallNumCount(mid, m, n); #计算乘法表中不大于mid的元素个数
        if (cnt >= k):
            high = mid;
        else:
            low = mid +1;
    return low;
# 在m，n的乘法表中，寻找不大于num的元素个数
def smallNumCount(num, m, n) :
    count = 0
    #对乘法表的每一行（每一行都是递增）进行搜索，muns[row][col] = row * col
    for i in range(1,m+1) :
        count += min(num/i, n);#num/i代表的是如果num也在第i行，它存在的列数，而一行最多只有n个
    return count;

m = int(input());
n = int(input());
k = int(input());
print(int(findKthNumber(m,n,k)))
