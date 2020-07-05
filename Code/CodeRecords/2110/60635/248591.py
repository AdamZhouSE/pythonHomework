num=int(input())


def isugly(num):
    if num == 1:
        return True
    while num % 2 == 0:
        num /= 2
    while num % 3 ==0:
        num /= 3
    while num% 5 ==0:
        num /= 5
    return num==1


print(isugly(num))