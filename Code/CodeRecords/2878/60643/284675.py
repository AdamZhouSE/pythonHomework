def find(n):
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    return sorted(lst,reverse=False)

if __name__=="__main__":
    n,length=input().split()
    n=int(n)
    length=int(length)
    buckets=input().split()
    buckets=[int(x) for x in buckets]
    lst=find(length)
    res=0
    for i in lst:
        if i in buckets:
            res=length//i
    print(res)