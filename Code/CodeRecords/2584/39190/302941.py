def func1(num):
    if num!=1 and num%3==1:
        return False
    else:
        return True

ip=int(input())
print(func1(ip))