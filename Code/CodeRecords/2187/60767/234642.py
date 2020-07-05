numOfTests =int(input())
K = []
element = []
NUM = []
for i in range(0,numOfTests):
    y = input().split()
    NUM.append(int(y[0]))
    K.append(int(y[1]))
    element.append(input().split())
for i in range(0,numOfTests):
    num = NUM[i]
    k = int(K[i])
    ele = element[i]
    max = 0
    for x in range(0,num-k+1):
        temp = 0
        for y in range(0,k):
            temp = temp + int(ele[x+y])
        if(temp>max):
            max = temp
    print(max)

