def isprime( i ):
    if i == 1:
        return 0
    flag = 0
    for k in range(2, i - 1):
        if i % k == 0:
            flag = 1
            break
    if flag == 0:
        return 1
    else:
        return 0


def prime(i):
    string = bin(int(i))
    num = 0
    for x in string:
        if x == "1":
            num = num + 1
    if isprime(num):
        return 1
    else:
        return 0


NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    res = 0
    num = input().split(" ")
    for k in range(int(num[0]), int(num[1])+1):
        if prime(k):
            res = res + 1
    result.append(res)
for i in result:
    print(i)
