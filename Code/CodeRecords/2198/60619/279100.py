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
print(length)
string = input()
print(string)
numbers = input().strip().split(" ")
result = 0
for i in range(len(string) - 1):
    for j in range(i + 1, len(string)):
        x = find_pre(i, j) + int(numbers[i]) ^ int(numbers[j])
        result = max(result, x)
print(result)
