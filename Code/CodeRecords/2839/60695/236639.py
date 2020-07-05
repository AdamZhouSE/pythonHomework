n = int(input())
namelist = [None]*n
for i in range(0, n):
    namelist[i] = input()
print("NO")
flag = False
for i in range(1, n):
    for j in range(0, i):
        if namelist[i] == namelist[j]:
            flag = True
    if flag:
        print("YES")
    else:
        print("NO")