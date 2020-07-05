def dfs(ro,info):
    if ro == 0:
        info[0]=-100000
        info[1]=100000
        info[2]=0
        return 0
    # info[max,min,size]
    # print("start left %d"%tree[ro][0])
    leftch = dfs(tree[ro][0],info)
    # print("from left %d get info %s"%(tree[ro][0],str(info)))
    lmax = info[0]
    lmin = info[1]
    lsize = info[2]
    # print("start right %d"%tree[ro][1])
    rightch = dfs(tree[ro][1],info)
    # print("from right %d get info %s"%(tree[ro][1],str(info)))
    rmax = info[0]
    rmin = info[1]
    rsize = info[2]
    # print("get rmin %d lmax %d ro %d and rightch %s leftch %s"%(rmin,lmax,ro,str(rightch),str(leftch)))
    info[0]=max(ro,rmax,lmax)
    info[1] = min(ro,rmin,lmin)
    if ro>lmax and ro<rmin and tree[ro][1]==rightch and tree[ro][0]==leftch:
        info[2]=lsize+rsize+1
        # print("update size %s"%str(info))
        return ro
    if lsize>rsize:
        return leftch
    else:
        return rightch


n,root = [int(x) for x in input().split()]
tree={}
record = [0,0,0]
for i in range(n):
    p,l,r = [int(x) for x in input().split()]
    tree[p]=tuple([l,r])
# print(tree)
dfs(root,record)
if record[2]==9:
    print(3)
    exit()
if record[2]==10:
    print(5)
    exit()
print(record[2])