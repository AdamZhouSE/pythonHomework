t = int(input())
for ind in range(t):
    length = int(input())
    numbers = [int(i) for i in input().strip().split(" ")]
    k = int(input())
    result = 0
    numbers.sort()
    for i in range(length-1):
        for j in range(i+1, length):
            if numbers[j] - numbers[i] == k:
                result += 1
    print(result)