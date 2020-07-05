N = 1000
a = [0]*N
b = [0]*N
L = [0]*N
R = [0]*N
pre = [0]*N
suc = [0]*N
n = 0
def dfs(now:int):
    if not now:return
    print(str(a[now])+" ",end='')
    dfs(L[now])
    dfs(R[now])

if __name__ == '__main__':
    n = eval(input())
    nums = input().split(' ')
    for i in range(1,n+1):
        a[i] = eval(nums[i-1])
        b[a[i]] = i
        pre[i] = i - 1
        suc[i] = i + 1
    for i in range(n,0,-1):
        pree = pre[a[i]]
        succ = suc[a[i]]
        if b[pree]>b[succ]:
            R[b[pree]] = i
        else:
            L[b[succ]] = i
        suc[pree] = succ
        pre[succ] = pree
    dfs(1)