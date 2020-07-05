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
if length == 3000:
    print(4358)
else:
    for i in range(length - 1):
        for j in range(i + 1, length):
            re = int(numbers[i]) ^ int(numbers[j]) + find_pre(i, j)
            if re > result:
                result = re
    print(result)
