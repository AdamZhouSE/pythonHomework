def arr10():
    n = input()
    sq = [int(x) for x in input().split(' ')]
    bt = [int(x) for x in input().split(' ')]
    tmp=sq.copy()
    pos=[]
    for num in bt:
        for i in range(len(tmp)):
            if(tmp[i]==num):
                tmp[i]=-1
                pos.append(i)
                
    pos.sort()
    for i in range(len(pos)):
        if(i!=len(pos)-1):
            print(sq[pos[i]],end='')
            print(' ',end='')
        else:
            print(sq[pos[i]])
    return

arr10()
