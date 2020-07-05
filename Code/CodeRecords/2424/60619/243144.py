t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    exist = False
    for n in numbers:
        if numbers.count(n)%2 == 1:
            print(n)
            exist = True
            break
    if not exist:
        print(0)