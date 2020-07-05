result=[]
handle=[]
def resolve(n,m):
    if(n%m!=0):
        resolve(n,m+1)
        return
    result.append((str)(m))
    if(n/m!=1):
        resolve((int)(n/m),m)
tests=(int)(input())
for i in range(0,tests):
    n=(int)(input())
    resolve(n,2)
    if(len(result)==1):
        print(0)
    else:
        for i in result:
            for j in i:
                handle.append((int)(j))
        sum=0
        for i in handle:
            sum+=i
        for i in (str)(n):
            sum-=(int)(i)
        if(sum==0):
            print(1)
        else:
            print(0)
    result=[]
    handle=[]