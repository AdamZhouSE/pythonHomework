t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    cout0 = 0
    cout1 = 0
    cout2 = 0
    for i in range(length):
        if int(numbers[i]) == 0:
            cout0 += 1
        elif int(numbers[i]) == 1:
            cout1 += 1
        else:
            cout2 += 1
    for i in range(cout0):
        numbers[i] = 0
    for i in range(cout1):
        numbers[cout0+i] = 1
    for i in range(cout2):
        numbers[cout0+cout1+i] = 2
    print(*numbers)
