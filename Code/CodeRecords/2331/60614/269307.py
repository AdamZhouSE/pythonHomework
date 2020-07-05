matrix=[]
maxn=0
init=[int(x) for x in input().split()]
for i in range(init[0]):
    matrix.append([int(x) for x in input().split()])
for i in matrix:
    for j in i:
        if maxn<j:
            maxn=j
def dichotomy():
    left=1
    right=maxn
    while(left<right):
        mid=int((left+right)/2)
        if(check(mid)>= init[0]-init[2]+1):#找第k大即找第n-k+1小
            right=mid
        else:
            left=mid+1
    return left

def check(mid):
    judge = [False,[-1] * init[1],[False]*init[1]]
    count=0
    for i in range(init[0]):
        judge[2]=[False] * init[1]
        if(find(i,mid,judge)[0]):
            count+=1
    return count

def find(row,lim,judge):
    for i in range(init[1]):
        if((not judge[2][i]) and matrix[row][i]<=lim):
            judge[2][i]=True
            if(judge[1][i]==-1 or find(judge[1][i],lim,judge)[0]):
                judge[1][i]=row
                judge[0]=True
                return judge
    judge[0]=False
    return judge

print(dichotomy())