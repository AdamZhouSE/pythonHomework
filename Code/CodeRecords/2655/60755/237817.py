def judge(i):
    for t in range(1000):
        if pow(2, t) == int(i):
            return 1
    return 0


NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = int(input())
    while not judge(num):
        num = num + 1
    result.append(num)
for i in result:
    print(i)