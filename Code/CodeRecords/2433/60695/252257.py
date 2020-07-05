sets = input().replace('[', '')
sets = sets.replace(']', '')
numbers = sets.split(",")
qujian = []
result = []
for i in range(0, int(len(numbers) / 2)):
    qujian.append([int(numbers[i*2]), int(numbers[i*2+1])])

for i in range(0, len(qujian)-1):
    j = i + 1
    while j < len(qujian):
        if qujian[i][1] >= qujian[j][0]:
            qujian[i] = [min(qujian[i][0], qujian[j][0]), max(qujian[i][1], qujian[j][1])]
            qujian.remove(qujian[j])
        else:
            j += 1
print(qujian)