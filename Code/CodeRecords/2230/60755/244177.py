a = int(input())
b = int(input())
c = int(input())
d = int(input())
res = []
fro = [a, b]
target = [c, d]
flag = 0
for i in range(100):
    if target[0]>target[1]:
        target[0] = target[0] - target[1]
    else:
        target[1] = target[1] - target[0]
    if target[0] == fro[0] and target[1] == fro[1]:
        flag = 1

if flag:
    print("True")
else:
    print("False")