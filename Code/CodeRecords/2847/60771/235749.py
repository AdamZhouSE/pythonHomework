#13
n = int(input())
ori = input().split(" ")
needYear = []
sum = 0
for i in range(0,n-1):
    needYear.append(int(ori[i]))
ori = input().split(" ")
a = int(ori[0])
b = int(ori[1])
for i in range(a-1,b-1):
    sum += needYear[i]
print(sum)