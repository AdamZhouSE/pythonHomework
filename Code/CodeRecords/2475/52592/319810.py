t = int(input())

for i in range(t):
    temp = []
    n = int(input())
    li = input().split(' ')
    for i in li:
        temp.append(int(i))
    temp = sorted(temp)
    #print(temp)
    result = []
    #print(type(temp[0]))
    res = 0
    for j in temp:
        if (j-1) not in temp:
            y = j+1
            while y in temp:
                y+=1
            res = max(res,y-j)
    print(res)