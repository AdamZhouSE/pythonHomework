data = list(eval(input()))
count = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] > 2 * data[j]:
            count += 1
print(count)
