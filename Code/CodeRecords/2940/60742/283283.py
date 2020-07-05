def judge(l,r,length):#判断该片段是否可缩减
    if (r-l+1)%length!=0:
        return False
    for i in range(1,r-l+2):
        if inp[l+i-1]!=inp[l+(i-1)%length]:
            return False
    return True

def digit(n):
    num = 0
    while n>0:
        num += 1
        n //= 10
    return num

def cutDown(l,r):
    global f,c
    if f[l][r]!=0:
        return
    if l==r:
        f[l][r] = 1
        c[l][r] = inp[l]
        return
    f[l][r] = r-l+1
    c[l][r] = inp[l:r+1]
    for i in range(l,r):
        cutDown(l,i)
        cutDown(i+1,r)
        if f[l][r]>f[l][i]+f[i+1][r]:
            f[l][r] = f[l][i]+f[i+1][r]
            c[l][r] = c[l][i]+c[i+1][r]
    for i in range(1,r):#为什么需要这一步：上面的操作是形式dp，这一步才是真正的dp
        #直观上理解，上面是搜索了所有可能的切分方式，本质上并没有进行任何缩减，而下面才是对cut出的每一段进行缩减
        if judge(l,r,i):
            cutDown(l,l+i-1)
            if f[l][r]>f[l][l+i-1]+2+digit((r-l+1)//i):
                f[l][r] = f[l][l+i-1]+2+digit((r-l+1)//i)
                c[l][r] = str((r-l+1)//i)+'('+c[l][l+i-1]+')'
    return

inp = input()
n = len(inp)
c = [[None]*n for _ in range(n)]
f = [[0]*n for _ in range(n)]
cutDown(0,len(inp)-1)
print(c[0][len(inp)-1])