t = input().split()
b = int(t[0])
length = int(t[1])
tL = input().split()
l = []
for var in tL:
    l.append(int(var))
result = 0
j = 0
while j < len(l):
    if l[j] % 2 == 0:
        j += 1
        continue
    else:
        temp = l[j] % 10
        c = len(l) - j - 1
        # print(c)
        tem = b
        if c == 0:
            tem = 1
        else:
            k = 0
            while k < c:
                tem = (tem * b)
                k += 1
        temp = (temp * tem)
        # print(temp)
        result += temp
        # print(result)
        j += 1
if result % 2 == 0:
    print("even")
else:
    print("odd")
