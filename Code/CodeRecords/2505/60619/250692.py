numbers = input().split(",")
n = len(numbers) - 1
actual = 0
for i in numbers:
    actual += int(i)
print(actual - int((n+1)*n/2))