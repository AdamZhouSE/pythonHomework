#19
ori = input().split(" ")
n = int(ori[0])
d = int(ori[1])
ori = input().split(" ")
num = [int(item) for item in ori]
count = 0
for i in range(1,n):
    while num[i] <= num[i-1]:
        num[i] += d
        count += 1
print(count)