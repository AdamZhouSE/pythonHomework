num = input().split(",")
numbers = [int(i) for i in num]
length = len(numbers)
i = length - 1
haveFind = False
h = 0
result = []
while i >= 0:
    h += 1
    if numbers[length-h] >= h > numbers[length - h - 1] :
        result.append(h)
    i -= 1
if len(result) == 0:
    print(-1)
else:
    print(result[len(result)-1])