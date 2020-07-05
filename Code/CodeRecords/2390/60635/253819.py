n=int(input())
src=[int(x) for x in input().split()]
ans = 0

def swap_in_array(x,y,k):
    for i in range(2**k):
        src[x+i],src[y+i]=src[y+i],src[x+i]
def fac(x):
    if x<=1:
        return 1
    return x*fac(x-1)
def judge(start,kind):
    for i in range(1,2**kind):
        if src[start+i]!=src[start+i-1]+1:
            return True
    return False
def dfs(kind,before):
    global ans
    if kind == n + 1:
        ans += fac(before)
        return
    opt1, opt2 = -1, -1
    l=2**(kind-1)
    for i in range(0,2**n,2*l):
        if judge(i,kind):
            if opt1==-1:
                opt1=i
            elif opt2==-1:
                opt2=i
            else:
                break
    if opt1==-1 and opt2==-1:
        dfs(kind+1,before)
        return
    elif opt1!=-1 and opt2==-1:
        swap_in_array(opt1,opt1+l,kind-1)
        dfs(kind+1,before+1)
        swap_in_array(opt1, opt1 + l, kind - 1)
    elif opt1!=-1 and opt2!=-1:
        for i in range(0,l+1,l):
            for j in range(0,l+1,l):
                swap_in_array(opt1+i,opt2+j,kind-1)
                if not judge(opt1,kind) and not judge(opt2,kind):
                    dfs(kind+1,before+1)
                    swap_in_array(opt1 + i, opt2 + j, kind-1)
                    break
                swap_in_array(opt1 + i, opt2 + j, kind-1)
dfs(1,0)
print(ans)