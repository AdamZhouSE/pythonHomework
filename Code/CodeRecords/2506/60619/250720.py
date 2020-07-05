numbers = input().split(",")
length = len(numbers)
listL = []
for i in range(length - 1):
    start = int(numbers[i])
    le = 1
    for j in range(i+1, length):
        if int(numbers[j]) > start:
            start = int(numbers[j])
            le += 1
    listL.append(le)
listL.sort()
print(listL[len(listL)-1])
