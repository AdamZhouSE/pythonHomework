num=int(input())
nearby=[[0]*3 for i in range(4*num*num)]
judge=[[[0]*(4*num*num) for j in range(3)] for k in range(4*num*num)]
count=[0]*(4*num*num)
def construct(first,second):
    count[first-1]+=1
    nearby[first-1][count[first-1]-1]=second
    count[second-1]+=1
    nearby[second-1][count[second-1]-1]=first
def dp(now,lBound,rBound):#now为当前值，b为父亲的值，a为另一边界
    father=0
    while(nearby[now-1][father]!=rBound):
        father+=1
    if judge[now-1][father][lBound-1]>0:
        return judge[now-1][father][lBound-1]
    left=0
    right=0
    if lBound>rBound:
        temp1=rBound+1
        temp2=lBound
    else:
        temp1=lBound
        temp2=rBound-1
    for i in range(3):
        if i!=father and temp1<=nearby[now-1][i] and nearby[now-1][i]<=temp2:
            if nearby[now-1][i]<now:
                left=max(left,dp(nearby[now-1][i],temp1,now))
            else:
                right=max(right,dp(nearby[now-1][i],temp2,now))
    judge[now-1][father][lBound-1]=left+right+1
    return judge[now-1][father][lBound-1]

units=[[[]for x in range(num)] for y in range(4)]
for i in range(4):
    for j in range(0,num):
        for k in range(2*j+1):
            units[i][j].append(int(input()))
for i in range(4):
    for j in range(1,num):
        for k in range(1,2*j,2):
            construct(units[i][j][k],units[i][j-1][k-1])
            construct(units[i][j][k],units[i][j][k-1])
            construct(units[i][j][k],units[i][j][k+1])
for i in range(num):
    construct(units[0][i][0],units[2][i][2*i])
    construct(units[1][i][0],units[0][i][2*i])
    construct(units[2][i][0],units[1][i][2*i])
    construct(units[3][i][0],units[0][num-1][2*num-2*i-2])
    construct(units[3][i][2*i],units[1][num-1][2*i])
    construct(units[3][num-1][2*i],units[2][num-1][2*num-2*i-2])
result=0
for i in range(4*num*num):
    left=0
    right=0
    for j in range(3):
        if nearby[i][j]<i:
            left=max(left,dp(nearby[i][j],1,i+1))
        else:
            right=max(right,dp(nearby[i][j],4*num*num,i+1))
    result=max(result,left+right+1)
print(result)