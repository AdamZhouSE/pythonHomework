cout = int(input())
for i in range(cout):
    length = int(input())
    numbers = input().split(" ")
    index = len(numbers)
    while index > 1:
        for j in range(index-1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
        index -= 1
    result = 0
    for j in range(length-2):
        for k in range(j+1, length-1):
            for m in range(k+1, length):
                if int(numbers[j])+int(numbers[k]) > int(numbers[m]) and int(numbers[m])-int(numbers[j])<int(numbers[k]):
                    result += 1
    print(result)