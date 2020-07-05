string = list(input())
ST = int(input())
numbers = []
for x in string:
    numbers.append(str(ST+ord(x)-ord('A')))

numbers = list(map(int,''.join(numbers)))

while len(numbers)>3:
    for i in range(len(numbers)-1):
        numbers[i] = (numbers[i]+numbers[i+1])%10
    numbers.pop()


if numbers[0] == 1 and numbers[1] == 0 and numbers[2] == 0:
    print('100')
else:
    numbers[0] = (numbers[0]+numbers[1])%10
    numbers[1] = (numbers[1]+numbers[2])%10
    print(numbers[0]*10+numbers[1],end = "")