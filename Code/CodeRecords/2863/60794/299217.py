h = int(input().split(" ")[1])
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
wild = 0
for i in range(len(a)):
    if a[i] > h:
        wild = wild + 2
    else:
        wild = wild + 1
print(wild)