n = int(input())
list = input().split()
count = 0.000000
for i in range(n):
    count = count + float(list[i])
print('{:.6f}'.format(count/n))