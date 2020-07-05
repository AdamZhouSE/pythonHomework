def detect(house,my):
    if(house[my] == 1):
        return 0
    cnt = 0
    for x in range(my + 1,len(house)):
        if(house[x] != 1):
            cnt += 1
        else:
            break
    while(my >= 0):
        if(house[my] != 1):
            cnt += 1
        else:
            break
        my -= 1
    return cnt

n,m = list(map(int,input().split(" ")))
house = []
for x in range(n):
    house.append(0)# 0表示正常 1表示被摧毁

last = []
while(m != 0):
    m -= 1
    ops = input().split(" ")
    if(ops[0] == 'D'):
        last.append(eval(ops[1]) - 1)
        house[eval(ops[1]) - 1] = 1
        #print(last,house)
    elif(ops[0] == 'R'):
        if(len(last) > 0):
            house[last[-1]] = 0
            del last[-1]
        #print(last,house)
    elif(ops[0] == 'Q'):
        print(detect(house,eval(ops[1]) - 1))