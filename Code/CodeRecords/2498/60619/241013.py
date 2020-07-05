oriStr = input()
numbers = oriStr[1:len(oriStr)-1].split(",")
odds = []
even = []
for i in numbers:
    if int(i) % 2 == 0:
        even.append(i)
    else:
        odds.append(i)
for i in range(int(len(numbers)/2)):
    numbers[2*i] = int(even[i])
    numbers[2*i+1] = int(odds[i])
print(numbers)