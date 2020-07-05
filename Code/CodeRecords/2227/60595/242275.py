def Test():
    n=int(input())
    k=int(input())
    print(F(n,k))

def F(n,k):
    total=pow(k,n)
    res=str(n)
    visit=[]
    visit.append(res)
    for i in range(1,total):
        temp=res[len(res)-n+1:n-1]
        j=k-1
        while(j>=0):
            key=temp+str(j)
            if(visit.count(key)!=0):
                res=res+str(j)
                visit.append(key)
                break
if __name__ == "__main__":
    Test()