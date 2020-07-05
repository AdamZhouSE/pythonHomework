numOfExp = int(input())
for i in range(numOfExp):
    numOfNum = int(input())
    list1 = list(input().split())
    counter = 0
    sign = -1
    for j in range(numOfNum):
        for k in range(numOfNum):
            if list1[k] == list1[j]:
                counter += 1
        if counter>numOfNum/2:
            sign = list1[j]
            break
        counter = 0
    print(sign)
