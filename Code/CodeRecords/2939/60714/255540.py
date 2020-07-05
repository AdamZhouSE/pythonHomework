k, m = [int(x) for x in input().split()]
num = [1]
pointA = 0
pointB = 0
for i in range(0, k - 1):
    if num[pointA] * 2 + 1 < num[pointB] * 4 + 5:
        num.append(num[pointA] * 2 + 1)
        pointA += 1
    elif num[pointA] * 2 + 1 > num[pointB] * 4 + 5:
        num.append(num[pointB] * 4 + 5)
        pointB += 1
temp = "".join([str(i) for i in num])
start = 0
ans = ""
while start + 1 < len(temp) and m > 0:
    if temp[start] < temp[start + 1]:
        m -= 1
    else:
        ans += temp[start]
    start += 1
ans += temp[start:]
print(temp)
print(ans, end="")
