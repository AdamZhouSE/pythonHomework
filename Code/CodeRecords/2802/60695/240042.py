nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])
a = input().split(" ")
num = [None]*n
max = 0
for i in range(0, n):
    num[i] = i + 1
while len(a) > 1:
    if int(a[0]) > m:
        a.append(str(int(a[0]) - m))
        num.append(num[0])
    a.remove(a[0])
    num.remove(num[0])
print(num[0])