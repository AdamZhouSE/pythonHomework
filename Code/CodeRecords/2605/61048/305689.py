def tree12():
    line1=input().split(' ')
    N,M=int(line1[0]),int(line1[1])
    arr=[int(x) for x in input().split(' ')]
    piles=[[i] for i in arr]
    pos={}
    for i in range(N):
        pos[arr[i]]=i
    for i in range(M):
        order=[int(k) for k in input().split(' ')]

        if(order[0]==1):
            tar  =  min(pos[arr[order[1]-1]],pos[arr[order[2]-1]])
            deleted=max(pos[arr[order[1]-1]],pos[arr[order[2]-1]])
            if(tar==-1 or deleted==-1):
                continue
            '''tar=min(order[1]-1,order[2]-1)
            deleted=max(order[1]-1,order[2]-1)'''
            for num in piles[deleted]:
                piles[tar].append(num)
                pos[num]=tar
            '''piles.remove(piles[deleted])'''
        if(order[0]==2):
            if(pos[arr[order[1]-1]]==-1):
                print(-1)
                continue
            min_val=min(piles[pos[arr[order[1]-1]]])
            print(min_val)
            piles[pos[arr[order[1]-1]]].remove(min_val)
            pos[min_val]=-1
    return

tree12()