a = [int(i) for i in input().split(",")]
b = [int(i) for i in input().split(",")]
maxNum = 0
for i in range(len(a)):
    for j in range(len(a)):
        num = abs(a[i]-a[j]) + abs(b[i]-b[j]) +abs(i-j)
        maxNum = max(maxNum,num)
print(maxNum)