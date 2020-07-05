a = int(input())
b = input()  # 1,0
nb = ''.join(e for e in b if e.isdigit())
num = len(nb)
res = 1
for i in range(0, num):  # 0 -> num-1
    res = pow(res, 10, 1337) * pow(a, int(nb[i]), 1337) % 1337
print(res)
