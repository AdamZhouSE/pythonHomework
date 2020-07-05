import functools as ft

def compare(x,y):
    length=min(len(x[1]),len(y[1]))
    for i in range(length):
        if x[1][i]>y[1][i]:
            return 1
        elif x[1][i]<y[1][i]:
            return -1
    if length==len(x[1]) and length==len(y[1]):
        if father[x[0]]<father[y[0]]:
            return -1
        elif father[x[0]]>father[y[0]]:
            return 1
        else:
            if x[0]<y[0]:
                return -1
            elif x[0]>y[0]:
                return 1
            else:
                return 0
    elif length==len(x[1]):
        return -1
    return 1


def get_dis(node):
    s=""
    while node!=root:
        s+=weight[node]
        node=father[node]
    s+=weight[root]
    return s


if __name__ == '__main__':
    n=int(input())
    root=1
    vertex=[i for i in range(0,n+1)]
    father=[0,1]+[0]*(n-1)
    relation=list(map(int,input().split(" ")))
    for i in range(len(relation)):
        father[i+2]=relation[i]
    weight = ['0'] + [c for c in input()]
    res=[]
    for i in range(1,n+1):
        res.append([i,get_dis(i)])

    res.sort(key=ft.cmp_to_key(compare))

    ans=[]

    for e in res:
        ans.append(e[0])

    print(*ans,end=' ')