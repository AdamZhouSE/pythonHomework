num = int(input())
res = []
for i in range(100):
    res.append(pow(3,i))
flag = 0
for i in res:
    if num == i:
        flag = 1
if flag:
    print("True")
else:
    print("False")