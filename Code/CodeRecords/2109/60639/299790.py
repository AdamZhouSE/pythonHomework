num = input()
sum=0
for i in range(len(num)):
    sum += int(num[i])
while sum>=10:
    num = str(sum)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])

print(sum)