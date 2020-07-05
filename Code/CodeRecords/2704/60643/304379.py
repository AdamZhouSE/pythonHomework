from typing import List
def solution(edges:List[List[int]],n)->List[List[int]]:
    p=[i for i in range(n)]
    res=[]
    def find(x):
        if p[x]==x:
            return x
        else:
            return find(p[x])
    def union(a,b):
        x=find(a)
        y=find(b)
        if x==y:
            res.append([a+1,b+1])#从index到值
        else:
            p[y]=x

    for edge in edges:
        u=edge[0]
        v=edge[1]
        union(u-1,v-1)#因为p数组中都是index值

    return res

if __name__=="__main__":
    lst=eval(input())
    n=len(lst)
    ans=solution(lst,n)
    for i in ans:
        print(i)