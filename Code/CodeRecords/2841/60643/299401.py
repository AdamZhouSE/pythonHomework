def XOR(lst):
    res=[]
    for i in range(0,len(lst)-1,2):
        tmp=lst[i]^lst[i+1]
        res.append(tmp)
    return res

def OR(lst):
    res=[]
    for i in range(0,len(lst)-1,2):
        tmp=lst[i]|lst[i+1]
        res.append(tmp)
    return res
def solution(lst,n):
    #共做n轮
    for cnt in range(n):
        if cnt%2==0:
            lst=OR(lst)
        else:
            lst=XOR(lst)
    res=lst
    return  res[0]

if __name__=="__main__":
    [n,m]=list(map(int,input().split()))
    lst=list(map(int,input().split()))
    for _ in range(m):
        tmp=lst
        [p,b]=list(map(int,input().split()))
        lst[p-1]=b
        ans=solution(tmp,n)
        print(ans)