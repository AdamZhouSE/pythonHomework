num1 = input()
num1 = num1[1: len(num1)-1].split(",")
num2 = input()
num2 = num2[1: len(num2)-1].split(",")
if num1==['']:
    num1 = num2
elif num2 != ['']:
    num1.extend(num2) 
for i in num1:
    if i == 'null':
        num1.remove(i)
for i in range(len(num1)):
    num1[i] = int(num1[i])
num1.sort()
print(num1)