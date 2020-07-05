import copy

t = int(input())
for i in range(0,t):
    n = int(input())
    dots = []
    count = 0
    for j in range(0,n):
        dots.append(list(map(int,input().split(' '))))
    temp = copy.copy(dots)
    while(len(temp) > 0):
        curX = temp[0][0]
        k = len([x for x in temp if x[0] == curX])
        if(k > 1):            
            count = count + int(k * (k - 1) / 2)
        temp = [x for x in temp if x[0] != curX]
    temp = copy.copy(dots)
    while(len(temp) > 0):
        curY = temp[0][1]
        k = len([x for x in temp if x[1] == curY])
        if(k > 1):          
            count = count + int(k * (k - 1) / 2)
        temp = [x for x in temp if x[1] != curY]
    print(count)