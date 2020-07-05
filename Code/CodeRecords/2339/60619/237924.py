t = int(input())
for index in range(t):
    len = int(input())
    numbers = input().split()
    result = 0
    for i in range(len-1):
        for j in range(i+1, len):
            if int(numbers[i]) > int(numbers[j]):
                result += 1
    print(result)
