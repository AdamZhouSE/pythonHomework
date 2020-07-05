
def brick():
    row=int(input())
    dfs(row-1)
    dfs(row-2)

def dfs(row):
    global total
    if row==0:
        total+=1
        return
    elif row==-1:
        return
    dfs(row-1)
    dfs(row-2)

if __name__=='__main__':
    global total
    T=int(input())
    for i in range(0,T):
        total=0
        brick()
        print(total)