t = int(input())
for ind in range(t):
    length = int(input())
    numbers = [int(i) for i in input().strip().split(" ")]
    k = int(input())
    result = 0
    appeared = []
    numbers.sort()
    for i in range(length-1):
        for j in range(i+1, length):
            if numbers[j] - numbers[i] == k and numbers[i] not in appeared:
                result += 1
                appeared.append(numbers[i])
    print(result)