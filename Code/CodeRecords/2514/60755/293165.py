a = list(input())
b = list(input())
flag = True
for i in a:
    if b.count(i)<a.count(i):
        flag = False
        break
print(flag)