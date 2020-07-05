aa = input()
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
x = 1
index = 0
for i in range(len(a)-1):
    if x == -1:
        break
    if a[i] > a[i+1]:
        x = x - 1
        index = i
if x == -1:
    print(-1)
else:
    if a[len(a)-1] > a[0] and x == 1:
        print(0)
    elif a[len(a)-1] > a[0] and x == 0:
        print(-1)
    else:
        print(len(a)-1-index)