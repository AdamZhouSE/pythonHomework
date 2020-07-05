num = input()
k = int(input())
length = len(num)
num = num[1:length-1].split(",")
for i in range(0, len(num)):
    num[i] = int(num[i])
num = sorted(num)
dis = []
for i in range(1, len(num)):
    dis.append(abs(num[i] - num[i-1]))
dis = sorted(dis)
i = 1
count = 1
minD = dis[0]
while count != k:
    if dis[i] != dis[i-1]:
        count += 1
    i += 1
print(dis[i-1])
