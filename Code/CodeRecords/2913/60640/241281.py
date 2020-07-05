"""
2.19
全为零的数组
为了得到全为0的数组
所有元素的和为偶数，并且最大数<和的一半
"""
n = int(input())
data = input().split(" ")
data_int = []
sum_n = 0
for i in range(0, n):
    data_int.append(int(data[i]))
    sum_n += int(data[i])
max_n = max(data_int)
if sum_n % 2 == 0 and max_n < (sum_n / 2):
    print("YES")
else:
    print("NO")
