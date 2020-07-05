input()
ls = list(map(int, input().split(" ")))
ls.sort()
a = ls[0]
flag = a
for i in ls:
    if i%a != 0:
        flag = -1
print(flag)