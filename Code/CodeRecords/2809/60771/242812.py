#26
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
length = 0
width = 0
num.sort()
mid = n//2
for i in range(0,mid):
    width += num[i]
for i in range(mid,n):
    length += num[i]
outcome = length*length + width*width
print(outcome)