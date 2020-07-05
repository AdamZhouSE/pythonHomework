a = input()
aa = a[1: len(a)-1].split(",")
b = []
for x in aa:
    b.append(int(x))
c = int(input())
x = 0
num = []
for i in range(len(b)):
    num.append(int(b[i]))
    if num[i] == c:
        x = 1
        print(i)
if x == 0:
    print(-1)