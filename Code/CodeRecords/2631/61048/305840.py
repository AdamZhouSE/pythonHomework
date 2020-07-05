def tree13():
    line1=input().split(' ')
    N,G=int(line1[0]),int(line1[1])
    revise=[]
    for i in range(N):
        revise.append([int(x) for x in input().split(' ')])
    revise.sort()
    cow_num=max(revise,key=lambda x:x[1])[1]
    cows=[G]*cow_num
    res=0
    max_tmp=0
    winner = []
    for record in revise:
        tmp = winner.copy()
        winner=[]
        cows[record[1]-1]+=record[2]
        for i in range(cow_num):
            if(cows[i]>max_tmp):
                max_tmp=cows[i]
                winner.append(i)
        for i in range(cow_num):
            if(cows[i]==max_tmp and i not in winner):
                winner.append(i)
        winner.sort()
        if(tmp!=winner):
            res+=1
        '''print(winner,max_tmp,cows)'''
    print(res,end='')
    return


tree13()