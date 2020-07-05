import bisect
def insert(tmp_ver,x,versions):
    tmp_ver.append(x)
    versions.append(sorted(tmp_ver))
    return versions


def remove(pre_ver,x,versions):
    p=-1
    for i in pre_ver:
        if i==x:
            p=pre_ver.index(i)
            break
    if p!=-1:
        new_ver=pre_ver[:p]+pre_ver[p+1:]
        versions.append(new_ver)
    else:
        versions.append(pre_ver)
    return versions


def quiry(pre_ver,x):
    tmp=sorted(pre_ver)
    p=tmp.index(x)
    rank=p+1
    return rank


def q_rank_of_X(pre_ver,x):
    return pre_ver[x-1]


def pre(pre_ver,x):
    tmp = sorted(pre_ver)
    pos=bisect.bisect_left(tmp,x)
    if pos==0:
        return -pow(2,31)+1
    else:
        return pre_ver[pos-1]


def succ(pre_ver,x):
    tmp = sorted(pre_ver)
    pos = bisect.bisect_right(tmp, x)
    if pos == len(pre_ver):
        return pow(2, 31) + 1
    else:
        return pre_ver[pos]

def solution(ops):
    versions=[[]]
    res=[]
    for op in ops:
        pre_ver=versions[op[0]].copy()#一定要加copy
        do,x=op[1],op[2]
        if do==1:
            versions=insert(pre_ver,x,versions)
        elif do==2:
            versions=remove(pre_ver,x,versions)
        elif do==3:
            res.append(quiry(pre_ver,x))
            versions.append(pre_ver)
        elif do==4:
            res.append(q_rank_of_X(pre_ver,x))
            versions.append(pre_ver)
        elif do==5:
            res.append(pre(pre_ver,x))
            versions.append(pre_ver)
        else:
            res.append(succ(pre_ver,x))
            versions.append(pre_ver)
    return res


if __name__=="__main__":
    n=int(input())
    ops=[]
    for _ in range(n):
        tmp=list(map(int,input().split()))
        ops.append(tmp)
    ans=solution(ops)
    for i in ans:
        print(i)