def isPer(num):
    i=1
    while i**2<=num:
        if i**2==num:
            return True
        i+=1
    return False

num=int(input())
print(isPer(num))