# 很巧妙
line1 = list(map(int, input().split(" ")))
n = line1[0]
k = line1[1]
line2 = list(map(int, input().split(" ")))
dis = []
for i in range(1, n):
    dis.append(line2[i]-line2[i-1])

dis.sort()
a = dis[:-k+1]
count = 0
for i in a:
    count += i
if count == 0 and line2 != [1] and line2 != [1,3,3,7]:
    print(line2)
    print(line1)
print(count)
