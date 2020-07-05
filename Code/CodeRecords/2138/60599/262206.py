"""
用pre_sum保存到第i个元素为止的 前缀和%k，因为倍数对结果的影响不大，而用余数有奇效

例如，nums=[11,2,4], k = 6
i=0: 11%6 = 5,
i=1: (5+2)%6 = 1
i=2: (1+4)%6 = 5
i=0和i=2时的结果相同，刚好2+4是6的倍数，返回True

结论：到每一位时都计算当前的累积和，并对k取模，保存起来，若出现相同的值，则存在符合要求的连续子数组

还要保证至少是两个数字
还要考虑k=0的情况
"""
nums=list(map(int,input().split(',')))
k=int(input())
if k == 0:
    print('00' in ''.join(map(str, nums)))
    exit()
pre_sum = {0:-1}
cur_sum = 0
for i, num in enumerate(nums):
    cur_sum = (num + cur_sum) % k
    if cur_sum in pre_sum and i - pre_sum[cur_sum] > 1:
        print(True)
        exit()
    if cur_sum not in pre_sum:
        pre_sum[cur_sum] = i
print(False)