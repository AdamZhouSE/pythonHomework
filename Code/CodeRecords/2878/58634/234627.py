#n个水桶，长度为k，第一行为n与k，第二行为每一个水桶能浇的长度，输出需要的最小时间，只能选一个水桶

a = input()
b = a.split(" ")
n = int(b[0])
k = int(b[1])
a = input()
lengths = [int(i) for i in a.split(" ")]
minNum = int(k)
for i in lengths:
    if k % i == 0 and minNum >= k / i:
        minNum = k/i
print(int(minNum))




