
num = int(input())
flag = 0
for i in range(1, int(pow(num, 0.5)) + 1):
    n = round((pow(num, 0.5) + i) * (pow(num, 0.5) - i))
    m = pow(n, 1/2)
    if m - int(m) == 0:
        flag = 1
        break
if flag:
    print("True")
else:
    print("False")