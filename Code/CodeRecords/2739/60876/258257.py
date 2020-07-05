k,n=map(int,input().split(","))
m=[]
t=0
def f(k,n,start):
    if k==1 and start<=n:
        return[[n]]
    elif k==1:
        return[[]]
    else:
        temp=[]
        for i in range(start,n//k+1):
            result=f(k-1,n-i,i+1)
            if result==[[]]:
                continue
            else:
                for item in result:
                    now=[i]
                    for items in item:
                        now.append(items)
                    temp.append(now)
        return temp
print(f(k,n,1))