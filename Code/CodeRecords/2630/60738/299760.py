num_list=eval(input())
N=len(num_list)
finish=False
i=0
j=0
que=[[num_list[i][j],i,j]]
routine=[num_list[0][0]]
exist=[[0,0]]
while(not finish):
    if i==N-1 and j==N-1:
        finish=True
    if i-1!=-1 and [i-1,j] not in exist:
        que.append([num_list[i-1][j],i-1,j])
        exist.append([i-1,j])
    if j-1!=-1 and [i,j-1] not in exist:
        que.append([num_list[i][j-1],i,j-1])
        exist.append([i,j-1])
    if i+1!=N and [i+1,j] not in exist:
        que.append([num_list[i+1][j],i+1,j])
        exist.append([i+1,j])
    if j+1!=N and [i,j+1] not in exist:
        que.append([num_list[i][j+1],i,j+1])
        exist.append([i,j+1])
    que.sort()
    routine.append(que[0][0])
    i=que[0][1]
    j=que[0][2]
    que.pop()
    
    
print(max(routine))
    