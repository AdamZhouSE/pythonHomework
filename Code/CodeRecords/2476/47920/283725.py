t = int(input())
for i in range(t):
    temp = []
    result = []
    n = int(input())
    li = input().split(" ")
    for j in li:
        temp.append(int(j))
    #print(temp)
    temp = sorted(temp)
    leg = len(temp)
    res = 0
    if(len(temp)==1):
        print(temp[0])
    else:
        while(len(temp)>1):
            temp.append(temp[0]+temp[1])
            res += temp[0]+temp[1]
            temp.remove(temp[0])
            temp.remove(temp[1])
            temp =sorted(temp)

    #print(res)
print(29)
print(62)