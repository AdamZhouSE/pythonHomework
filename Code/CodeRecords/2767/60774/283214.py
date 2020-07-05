t = int(input())
for i in range(0,t):
    target = int(input())
    way = []
    numOfThree = 0
    while(3 * numOfThree < target):
        if((target - 3 * numOfThree) % 5 == 0):
            way.append([numOfThree,int((target - 3 * numOfThree) / 5)])
        numOfThree  = numOfThree + 1
    count = len(way)
    for w in way :
        if(w[1] > 1):
            count = count + int(w[1] / 2)
    print(count)