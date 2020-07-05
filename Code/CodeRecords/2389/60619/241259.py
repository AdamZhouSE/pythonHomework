t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    for i in range(0, length, 2):
        if i+1 > length-1:
            print(numbers[i], end=" ")
        else:
            print(numbers[i+1]+" "+numbers[i], end=" ")
    print()
