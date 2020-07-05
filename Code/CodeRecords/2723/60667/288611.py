t = int(input())
for i in range(t):
    li = list(map(int, input()))
    temp = 0
    while True:
        temp = sum(li)
        if temp >= 10:
            li = list(map(int, str(temp)))
        else:
            break
    print(temp)    