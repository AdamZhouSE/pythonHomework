def getvalue():
    global stack,minn
    newstack=sorted(stack,reverse=True)
    minn=min(newstack[k-1],minn)
    return

def search(depth):
    global n,m,nums,selected_col,stack
    if depth==n:
        getvalue()
        return
    for i in range(0,m):
        if not selected_col[i]:
            selected_col[i]=True
            stack.append(nums[depth][i])
            search(depth+1)
            selected_col[i]=False
            stack.pop()
    return

n,m,k=map(int,input().split())
nums=[]
for i in range(0,n):
    nums.append(list(map(int,input().split())))
selected_col=[False for i in range(0,m)]
stack=[]
minn=99999999999
search(0)
print(minn)