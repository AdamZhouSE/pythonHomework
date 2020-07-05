def happy(i):

    for k in range(1000):
        if i == "1":
            return 1
        else:
            sum = 0
            for x in str(i):
                sum = sum + int(x) * int(x)
            i = str(sum)
    return 0


NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = int(input())
    for t in range(num+1, num+1000):
        if happy(t):
            result.append(t)
            break
for i in result:
    print(i)