length = int(input())
numbers = [int(i) for i in input().strip().split(" ")]
result = 0
while len(numbers) > 1:
    numbers.sort()
    result = result + numbers[0]+numbers[1]
    numbers.append(numbers[0]+numbers[1])
    del(numbers[0])
    del(numbers[0])
print(result)