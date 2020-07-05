couples = eval(input())
count = 0
for i in range(0, len(couples) , 2):
    if couples[i + 1] == couples[i] ^ 1:
        continue
    else:
        for j in range(i + 1, len(couples)):
            if couples[j] == couples[i] ^ 1:
                couples[i + 1], couples[j] = couples[j], couples[i + 1]
                break
        count += 1
print(count)

