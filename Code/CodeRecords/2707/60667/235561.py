couples = eval(input())
num = len(couples)
count = 0
for c in range(num):
    couples[c] = int(couples[c]/2)
for i in range(0, num, 2):
    for j in range(i+1, num, 1):
        if j - i > 1:
            if couples[i] == couples[j]:
                temp = couples[i+1]
                couples[i+1] = couples[j]
                couples[j] = temp
                count = count + 1
print(count)