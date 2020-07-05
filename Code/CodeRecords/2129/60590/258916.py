num = int(input())

def evenFunc(number):
    times = 0
    while number != 1:
        number = number/2
        times+=1
    return times

res = 0
if num % 2 == 0:
    res = evenFunc(num)
    print(res)
else:
    num = num - 1
    res = evenFunc(num)+1
    print(res)
print(res)