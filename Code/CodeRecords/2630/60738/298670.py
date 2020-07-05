num_list=eval(input())
N=len(num_list)
finish=False
i=0
j=0
que=[[num_list[i][j],i,j]]
routine=[]
while(not finish):
    if i+1==N and j+1==N:
        break
    if i+1==N:
        que.append([num_list[i][j+1],i,j+1])
        que.sort()
        i=que[0][1]
        j=que[0][2]
        routine.append(que[0][0])
        que.pop()
    elif j+1==N:
        que.append([num_list[i+1][j],i+1,j])
        que.sort()
        i=que[0][1]
        j=que[0][2]
        routine.append(que[0][0])
        que.pop()
    else:
        que.append([num_list[i][j+1],i,j+1])
        que.append([num_list[i+1][j],i+1,j])
        que.sort()
        i=que[0][1]
        j=que[0][2]
        routine.append(que[0][0])
        que.pop()
print(max(routine))
    