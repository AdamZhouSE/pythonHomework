from collections import defaultdict


def C_op(i, j,pep_in_room):
    for ky, val in pep_in_room.items():
        if i in val:
            val.remove(i)
            break
    pep_in_room[j].append(i)
    return pep_in_room

def solution(n,m,ops):
    done=[]
    res=[]
    pep_in_room=defaultdict(list)
    pep_in_room[0]=[i for i in range(n)]
    for op in ops:
        if op[0]=="C":
           pep_in_room = C_op(op[1]-1,op[2]-1,pep_in_room)
        elif op[0]=="W":
            l,r=op[1],op[2]
            dots=0
            for i in range(l-1,r):#[l-1:r+1]
                tmp=pep_in_room.get(i)
                if tmp==None or len(tmp)==0:
                    continue
                elif set(tmp) in done:
                    continue
                else:
                    dots+=len(tmp)
                    done.append(set(tmp))#如果不加set的话done中已经加进去的内容会随着pep...的改变而改变
            res.append(dots)
    return res
if __name__=="__main__":
    [n,m,t]=list(map(int,input().split()))
    ops=[]
    for _ in range(t):
        tmp=input().split()
        tmp[1],tmp[2]=int(tmp[1]),int(tmp[2])
        ops.append(tmp)
    res=solution(n,m,ops)
    for i in res:
        print(i)
