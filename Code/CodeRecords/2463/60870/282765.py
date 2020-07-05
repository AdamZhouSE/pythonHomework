numbers = input().split(',')
numbers = [int(x) for x in numbers]
target = int(input())
control = 0
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print('[' + str(i + 1) + ', ' + str(j + 1) + ']')
            control = 1
            break
    if control == 1:
        break
if control == 0:
    print('None')