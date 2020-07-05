string = input().split("+")
numbers = []
down = []
for temp in string:
    if('-' in temp):
        temp = temp.split("-")
        if(temp[0] != ''):
            num1 = list(map(int,temp[0].split("/")))
            if(num1[1] not in down):
                down.append(num1[1])
            numbers.append(num1)
        num2 = list(map(int,temp[1].split("/")))
        if(num2[1] not in down):
            down.append(num2[1])
        num2[0] = -num2[0]
        numbers.append(num2)
    else:
        temp = list(map(int,temp.split("/")))
        if(temp[1] not in down):
            down.append(temp[1])
        numbers.append(temp)

res2 = 1
for m in down:
    res2 *= m
res1 = 0
for x,y in numbers:
    res1 += x * int(res2 / y)
if(res1 == 0):
    print("0/1")
else:
    for n in range(2,res2 + 1):
        if(res1 % n == 0 and res2 % n == 0):
            res1 = int(res1/n)
            res2 = int(res2/n)
            if(res2 == 1):
                break
    print(str(res1) +"/" + str(res2))