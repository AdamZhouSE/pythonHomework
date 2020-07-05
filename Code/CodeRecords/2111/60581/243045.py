str = int(input())

def judgeNumber(number):
    while number % 2 == 0:
        number = number / 2

    while number % 5 == 0:
        number = number / 5

    while number % 3 == 0:
        number = number / 3

    if number == 1:
        return True
    else:
        return False

count = 0
start = 1
while True:
    if judgeNumber(start):
        count += 1
        if count == str:
            print(start)
            break
    start += 1