t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    odds = 0
    evens = 0
    for i in range(length):
        if i%2 == 0:
            odds += int(numbers[i])
        else:
            evens += int(numbers[i])
    print(max(odds, evens))