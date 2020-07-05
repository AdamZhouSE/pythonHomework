dict1 = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
n = [int(i) for i in list(input())]
tmp = [int(pow(10, len(n) - i - 1)) for i in range(len(n))]
n = list(zip(n, tmp))
s = ''
for i in n:
    if i[0] == 9:
        s += dict1[i[1]] + dict1[i[1] * 10]
    elif i[0] == 4:
        s += dict1[i[1]] + dict1[i[1] * 5]
    else:
        if i[0] == 5:
            s += dict1[i[1] * 5]
            i[0] -= 5
        s += dict1[i[1]] * i[0]
print(s)