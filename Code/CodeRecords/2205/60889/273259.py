def handShake(num):
    if num == 2:
        return 1
    if num == 0:
        return 1
    else:
        times = 0
        for i in range(0,num-1,2):
            times = times + handShake(i) * handShake(num-2-i)
        return times

numOfInput = int(input())
for i in range(numOfInput):
    numOfPeople = int(input())
    print(handShake(numOfPeople))