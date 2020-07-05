matrix=eval(input())
seas=[]
lands=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if(matrix[i][j])==1:
            lands.append([i,j])
        else:
            seas.append([i,j])
if((not lands) or (not seas)):
    print(-1)
else:
    distances=[]
    for sea in seas:
        distance=1000
        for land in lands:
            distance=min(distance,abs(land[0]-sea[0])+abs(land[1]-sea[1]))
        distances.append(distance)
    remotesea=seas[distances.index(max(distances))]
    ans=100000
    for land in lands:
        ans=min(ans,abs(remotesea[0]-land[0])+abs(remotesea[1]-land[1]))
    print(ans)