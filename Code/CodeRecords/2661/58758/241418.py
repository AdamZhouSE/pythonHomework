count = int(input())
ans = []
for i in range(0, count):
    num = int(input())
    num1 = 0
    num0 = 0
    str_num = bin(num)[2:]
    for j in range(0, len(str_num)):
        if str_num[j] == '0':
            num0 += 1
        else:
            num1 += 1
    ans.append(num1 ^ num0)
for k in ans:
    print(k)
