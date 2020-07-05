n = int(input())
temp = n
count = 0
while temp > 0:
    temp = int(temp/10)
    count += 1
if n == pow(10, count-1):
    s = ''
    for i in range(count-1):
        s += '9'
    print(s)
else:
    for i in range(2, n):
        res = list()
        temp = n
        while temp > 0:
            res.append(temp % i)
            temp = int(temp / i)
        flag = True
        for j in res:
            if j != 1:
                flag = False
                break
        if flag:
            print(i)
            break


