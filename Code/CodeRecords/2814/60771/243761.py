#28
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
num.sort()
satisfy = 1
for i in range(1,n):
    sum_all = 0
    for j in range(0,i):
        sum_all += num[j]
    if sum_all <= num[i]:
        satisfy += 1
print(satisfy)