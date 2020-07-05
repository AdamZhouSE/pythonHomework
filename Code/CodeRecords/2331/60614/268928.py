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
    count=0
    judge=[0]*init[1]
    for i in range(init[0]):
        visited=[False] * init[1]
        if(find(i,mid,visited,judge)):
            count+=1
    return count

def find(row,lim,visited,judge):
    for i in range(init[1]):
        if((not visited[i]) and matrix[row][i]<=lim):
            visited[i]=True
            if(judge[i]==0 or find(judge[i],lim,visited,judge)):
                judge[i]=row
                return True
    return False

print(dichotomy())