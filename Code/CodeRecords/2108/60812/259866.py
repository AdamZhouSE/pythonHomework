import math
s = input()
n = len(s)
num = 0
if int(s) > 0:
    temp, l = 1, [0, 1]
    for i in range(1, n-1):
        temp = 10 * temp + math.pow(10, i)
        l.append(temp)
    for i in range(n):
        if s[i] != '0':
            num += int(s[i])*l[n-1-i]
            if s[i] > '1':
                num += math.pow(10, n-1-i)
            elif i != n-1:
                num += int(s[i+1:])+1
            else:
                num += 1
print(int(num))
