all = input().split(",")
all.sort()
num = len(all)
sum = 0
for i in range(1,len(all)):
    sum = sum + int(all[i])
res = num * (sum - int(all[0])) - (sum + int(all[0]))
res = res/(num - 1)
print(int(res))