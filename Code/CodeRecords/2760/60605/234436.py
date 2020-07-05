t = int(input())
li = []
for i in range(t):
    a = input().split(" ")
    b = []
    b.append(int(a[0]))
    b.append(int(a[1]))
    li.append(b)

for i in range(t):
    if (li[i][0] % 2 == 0):
        li[i][0] //= 2
    else:
        li[i][0] //= 2
        li[i][0] += 1
    print(li[i][1] * li[i][0])