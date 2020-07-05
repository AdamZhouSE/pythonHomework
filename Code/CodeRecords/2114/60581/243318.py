str = int(input())

count = 1
while count*count < str:
    count += 1

count -= 1
number1 = 0
left = str
for i in range(0,count):
    while left >= pow(count-i,2):
        left -= pow(count-i,2)
        number1 += 1
number2 = 0
left = str
for i in range(1,count):
    while left >= pow(count - i, 2):
        left -= pow(count - i, 2)
        number2 += 1
print(min(number1,number2))
