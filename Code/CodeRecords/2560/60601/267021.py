n = eval(input())
for i in range(n):
    k = eval(input())
    num = list(map(int,input().split(' ')))
    m = eval(input())
    ID = []
    nu = list(set(num))
    for i in nu:
        ID.append([i,num.count(i)])
    ID.sort(key=lambda x:x[1])
    #print(ID)
    index = 0
    while(m!=0):
        if ID[index][1] == 1:
            ID[index][1] = 0
            m = m - 1
            index = index + 1
            continue
        if m == ID[index][1]:
            m = 0
            ID[index][1] = 0
            break
        if m < ID[index][1]:
            ID[index][1] -= m
            m = 0
            continue
        if m>ID[index][1]+1:
            m = m - ID[index][1]
            ID[index][1] = 0
            index = index + 1
            continue
        elif m == ID[index][1]+1:
            index += 1
            continue
    count = 0
    for i in ID:
        if i[1]!=0:
            count+=1
    print(count)

