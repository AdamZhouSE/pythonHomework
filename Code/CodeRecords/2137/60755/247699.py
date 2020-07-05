num = int(input())
all = []
for i in range(1, num):
    if num % i == 0:
        all.append(i)
res = 0
for i in all:
    res = res + i
print(res==num)