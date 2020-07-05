def search16():
    strs=input()[1:-1].split(',')
    res=minDepth(strs,0)
    print(res)
    return


def minDepth(strs,root):
    if strs[root]=='null':
        return 0
    else:
        if 2*root+1>=len(strs):
            return 1
        elif(strs[2*root+1]=='null' or strs[2*root+2]=='null'):
            return 1
        else:
            return min(minDepth(strs,2*root+1),minDepth(strs,2*root+2))+1

search16()