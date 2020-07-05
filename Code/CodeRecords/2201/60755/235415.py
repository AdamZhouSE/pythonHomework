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


#print(input())
#print(input())
#print(input())
NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    string = input()
    num = int(string[0]) + int(string[-1])
    res = num + 1
    while not isprime(res):
        res = res + 1
    result.append(res - num)
for i in result:
    print(i)
    