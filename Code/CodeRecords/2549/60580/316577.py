number = input().split()
value = input().split()
for i in range(int(number[0])):
    value[i] = int(value[i])
value.sort(reverse=True)
for i in range(int(number[1])):
    temp = input().split()
    if temp[0] == '1':
        print(value[int(temp[1]) - 1])
    else:
        value.append(int(temp[1]))
        value.sort(reverse=True)
