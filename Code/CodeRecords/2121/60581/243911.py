str = int(input())

def rank(number):
    i = 1
    answer = 1
    while i < number:
        i += 1
        answer *= i
    return answer

numberList = []
numberList.append(1)
numberList.append(10)

i = 1

while i <= 10:
    i += 1
    point = int(9 * rank(9) / rank(10-i) + numberList[i-1])
    numberList.append(point)

if str<=10:
    print(numberList[str])
else:
    print(numberList[10])