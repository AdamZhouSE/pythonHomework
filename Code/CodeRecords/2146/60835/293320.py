for q in range(int(input())):
    nmk = list(map(int, input().split()))
    shop = list(map(int, input().split()))
    road = []
    time = []
    his = set()
    for n in range(nmk[0]):
        road.append([])
        time.append([])
    for m in range(nmk[1]):
        tem = list(map(int, input().split()))
        road[tem[0] - 1].append(tem[1] - 1)
        time[tem[0] - 1].append(tem[2])
    need = list(map(int, input().split()))
    k = nmk[2]
    now = need[0] - 1
    res = 0
    drink = 0
    eat = 0
    finish = True
    #print(road,time)
    
    #find path
    while True:
        #drink or eat
        if shop[now] == 1:
            drink = drink + 1
        else:
            eat = eat + 1
        #is finish
        if now == (need[1] - 1):
            break
        
        if now not in his:
            his.add(now)
        else:
            finish = False
            break
        
        print(now)
        tem = min(time[now])
        index = time[now].index(tem)
        res = res + tem
        now = road[now][index]
    
    print(drink, eat)
    if finish:
        if (max(drink,eat) - min(drink,eat)) <= k:
            print(res)
        else:
            print(-1)
    else:
        print(-1)