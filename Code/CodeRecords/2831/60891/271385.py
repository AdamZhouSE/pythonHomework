n = int(input())
d = [int(i) for i in input().split()]
s_t = [int(i) for i in input().split()]
s_t.sort()
s = s_t[0]
t = s_t[1]
sum_ = 0
for i in d:
    sum_ += i
dis = 0
for i in range(t - s):
    dis += d[i + s - 1]
if dis > sum_ // 2:
    dis = sum_ - dis
print(dis)