t = int(input())
for ind in range(t):
    length = int(input())
    numbers = [int(i) for i in input().strip().split(" ")]
    maxArea = 0
    for i in range(length):
        if numbers[i] > maxArea:
            maxArea = numbers[i]
        if i < length - 1:
            height = numbers[i]
            for j in range(i+1, length):
                if numbers[j] < height:
                    height = numbers[j]
                if height * (j-i+1) > maxArea:
                    maxArea = height * (j-i+1)
    print(maxArea)
