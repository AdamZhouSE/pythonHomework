numbers = input().split(",")
i=0
while i<len(numbers):
    numbers[i] = int(numbers[i])
    i=i+1
numbers.sort()
print(max(numbers[0]*numbers[1],numbers[len(numbers)-2]*numbers[len(numbers)-3])*numbers[len(numbers)-1])