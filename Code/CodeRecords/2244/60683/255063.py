N = eval(input())
candidate = N 


def isPrime(num):
    end = int(pow(num, 1 / 2))+1
    flag = True
    for i in range(2, end + 1):
        if num % i == 0:
            flag = False
            break
    return flag


def isPali(num):
    s = str(num)
    return s[::-1] == s


while True:
    if isPrime(candidate) and isPali(candidate):
        break
    candidate += 1
print(candidate)
