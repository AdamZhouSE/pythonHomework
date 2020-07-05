#33
# 这题有n+1的塔。0号塔没写出来，注意一下
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
dollar = num[0] # 一开始高度0，保证能量不负，一定要氪这么多的
power = 0
for i in range(1,n):
    sub = num[i-1] + power - num[i]
    if sub < 0:
        dollar += abs(sub)
        num[i-1] += abs(sub)
    power += num[i-1]-num[i]
print(dollar)