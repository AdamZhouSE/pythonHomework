m = int(input())
n = int(input())
ops = int(input())
opsOnM = [m]
opsOnN = [n]
for i in range(0,ops):
    op = input().split(',')
    opsOnM.append(int(op[0]))
    opsOnN.append(int(op[1]))
print(min(opsOnM) * min(opsOnN))