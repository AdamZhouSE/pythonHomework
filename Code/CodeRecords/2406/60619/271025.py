length = int(input())
numbers = []
target = []
for i in range(length):
    x = int(input().strip())
    numbers.append(x)
    target.append(x)
target.sort()
maxDi = 0
start = 0
end = 0
for i in numbers:
    if abs(numbers.index(i) - target.index(i)) > maxDi:
        maxDi = abs(numbers.index(i) - target.index(i))
        start = numbers.index(i)
        end = target.index(i)
    elif abs(numbers.index(i) - target.index(i)) == maxDi and numbers.index(i) > target.index(i):
        start = numbers.index(i)
        end = target.index(i)
temp = numbers[end]
numbers[end] = numbers[start]
numbers[start] = temp
count = 0
l = length - 1
while l > 0:
    for i in range(l):
        if numbers[i] > numbers[i+1]:
            temp = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i] = temp
            count += 1
    l -= 1
print(count)