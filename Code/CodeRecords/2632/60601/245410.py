def Q(house:list,n:int):
    if house[n] == 'Null':
        return 0#被堵死和摧毁
    else:
        count = 1
        w = n - 1
        while w>=0:
            if house[w]!='Null':
                w = w - 1
                count = count + 1
            else:
                break
        s = n +1
        while s<len(house):
            if house[s] != 'Null':
                s = s + 1
                count = count + 1
            else:
                break
        return count

if __name__ == '__main__':
    line = input().split(' ')
    n = int(line[0])
    m = int(line[1])
    house = ['Null']
    D = []
    for i in range(1,n+1):
        house.append(i)
    for i in range(m):
        order = input()
        if order == 'R':
            if len(D)!=0:
                house[D[-1]] = D[-1]
                D = D[1:-1]
        else:
            order = order.split(' ')
            if order[0] == 'D':
                house[int(order[1])] = 'Null'
                D.append(int(order[1]))
            else:
                print(Q(house,int(order[1])))