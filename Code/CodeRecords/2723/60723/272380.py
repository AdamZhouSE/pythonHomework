def summary(number):
    string=str(number)
    total=0
    for i in range(len(string)):
        total=total+int(string[i])
    return total
num=int(input())
for i in range(num):
    number=int(input())
    while number>9:
        number=summary(number)
    print(number)