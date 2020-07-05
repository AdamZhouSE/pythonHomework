#09
ori = input().split(",")
num = [int(item) for item in ori]
K = int(input())
num.sort()
if len(num) == 1:
    print(0)
    exit(0)
minGap = 100
for i in range(0,len(num)-1):
    if num[i+1] - num[i] < minGap:
        minGap = num[i+1] - num[i]
if minGap - 2*K <= 0:
    minGap = 0
else:
    minGap -= 2*K
print(minGap)