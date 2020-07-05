#29
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
num.sort()
i = 0
while len(num) > 1:
    if i%2 == 0:
        num.remove(num[len(num)-1])
    else:
        num.remove(num[0])
    i += 1
print(num[0])