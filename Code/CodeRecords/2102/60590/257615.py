num = int(input())

def IsPrime(num):
    if num == 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

res = []
for i in range(1, num):
    if IsPrime(i):
        res.append(i)

print(res.__len__())