# 给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中。
#
# 在此过程之后，我们得到一些数组 B。
#
# 返回 B 的最大值和 B 的最小值之间可能存在的最小差值。

li = list(eval("["+input()+"]"))
k = int(input())
li = sorted(li)
minDiff = 9999999
for i in li:
    i -= k
for i in range(len(li)):
    li[i] += (2*k)
    newli = sorted(li.copy())
    minDiff = min(minDiff, newli[len(li)-1]-newli[0])
print(minDiff)
