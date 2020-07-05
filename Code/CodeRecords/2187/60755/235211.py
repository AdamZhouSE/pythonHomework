NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    all_num = input().split(" ")
    all_eg = input().split(" ")
    sumofNum = 0
    maxofNum = int(all_eg[0])
    for k in range(int(all_num[0])-int(all_num[1])+1):
        for x in range(int(all_num[1])):
            sumofNum = sumofNum + int(all_eg[x+k])
        if maxofNum < sumofNum:
            maxofNum = sumofNum
        sumofNum = 0
    result.append(maxofNum)
for i in result:
    print(i)