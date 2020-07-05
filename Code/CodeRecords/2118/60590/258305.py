num = int(input())

def is3Power(num):
    while num > 1:
        num = num /3
    if num == 1:
        return True
    else:
        return False

print(is3Power(num))