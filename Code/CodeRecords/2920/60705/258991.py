# 很巧妙
line1 = list(map(int, input().split(" ")))
n = line1[0]
k = line1[1]
line2 = list(map(int, input().split(" ")))
dis = []
for i in range(1, n):
    dis.append(line2[i]-line2[i-1])

dis.sort()
if k > 1:
    a = dis[:-k+1]
else:
    a = dis
count = 0
for i in a:
    count += i
print(count)
