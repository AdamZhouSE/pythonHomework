def final_loc_ori(opes:list,n):
    current_ori='N'
    current_loc=[0,0]
    up={'N':'N','S':'S','W':'W','E':'E'}
    down={'N':'S','S':'N','W':'E','E':'W'}
    left={'N':'W','S':'E','W':'S','E':'N'}
    right={'N':'E','S':'W','W':'N','E':'S'}
    for i in range(n):
        move,steps=opes[2*i],int(opes[2*i+1])
        if move=='U':
            current_ori=up.get(current_ori)
        elif move=='D':
            current_ori=down.get(current_ori)
        elif move=='L':
            current_ori=left.get(current_ori)
        elif move=='R':
            current_ori=right.get(current_ori)

        if current_ori=='N':current_loc[1]+=steps
        elif current_ori=='S':current_loc[1]-=steps
        elif current_ori=='W':current_loc[0]-=steps
        elif current_ori=='E':current_loc[0]+=steps
    final_dis=int(pow(pow(current_loc[0],2)+pow(current_loc[1],2),0.5))
    print(final_dis,current_ori)
    return 0

cases=int(input())
for i in range(cases):
    n=int(input())
    opes=input().split()
    final_loc_ori(opes,n)