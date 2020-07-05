def find_pre(pos1, pos2):
    x = 0
    while pos2 < length:
        if string[pos2] == string[pos1]:
            x += 1
        else:
            break
        pos1 += 1
        pos2 += 1
    return x


length = int(input())
string = input()
numbers = input().strip().split(" ")
result = 0
minIndex = 0
maxIndex = 0
for i in range(1, length):
    if int(numbers[i]) < int(numbers[minIndex]):
        minIndex = i
    if int(numbers[i]) > int(numbers[maxIndex]):
        maxIndex = i
result = int(numbers[minIndex]) ^ int(numbers[maxIndex]) + find_pre(min(minIndex,maxIndex),max(minIndex,maxIndex))
print(result)
