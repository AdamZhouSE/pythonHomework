numbers = input().split(',')
numbers = [int(x) for x in numbers]
target = int(input())
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print('[' + str(i + 1) + ', ' + str(j + 1) + ']')
            break