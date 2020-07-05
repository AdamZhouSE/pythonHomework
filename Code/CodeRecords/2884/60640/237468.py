"""
2.18
侦查单位
"""
line1 = input().split()
n = int(line1[0])
d = int(line1[1])
data = input().split()
data_num = []
count = 0
for i in range(0, n):
    data_num.append(int(data[i]))
for i in range(0, n):
    for j in range(i+1, n):
        diff = abs(data_num[i]-data_num[j])
        if diff <= d:
            count += 1
# 侦察单位（a1, a2）和（a2, a1）应视为不同
count *= 2
print(count)
