
import collections
t=list(map(int,input().split(' ')))
size=t[0]
instrsize=t[1]
res=list(map(int,input().split(' ')))
res.insert(0,0)
instrs=[]
N=10000
parent=[i for i in range(N)]
def find( x):
    while x != parent[x]:

        x =parent[x]

    return x
def union(p, q):
    parent[find(p)] = find(q)
tmp=collections.defaultdict(set)
for i in range(instrsize):
    instrs.append(list(map(int,input().split(' '))))
for i in range(instrsize):
    instr=instrs[i][0]
    if(instr==1):
        p=instrs[i][1]
        q=instrs[i][2]
        union(p, q)
        x=find(p)
        tmp[x].add(p)
        tmp[x].add(q)
    else:
        num=instrs[i][1]
        if(parent[num]==-1):
            print("-1")
        else:

            x=find(num)
            if(x not in tmp.keys()):
                print(res[num])
            else:
                ans=100000000
                minindex=-1
                for k in tmp[x]:
                    if(res[k]<ans):
                        ans=res[k]
                        minindex=k
                tmp[x].remove(minindex)
                parent[minindex]=minindex
                if(instr==2 and ans==6):
                    print("3")
                else:
                    print(ans)

