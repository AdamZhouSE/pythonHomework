num = eval(input())
re = []
num = sorted(num)
count = 0
i = 0
while count < len(num):
    if count % 2 == 0:
        re.append(num[i])
    else:
        re.append(num[len(num) - 1 - i])
        i += 1
    count += 1
print(re)