numbers = input().split(",")
for i in numbers:
    if numbers.count(i) > 1:
        print(i)
        break
