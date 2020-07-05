n=int(input())
start=[]
end=[]
length=[]
for i in range(0,n-1):
    a,b,c=map(int,input().split(" "))
    start.append(a)
    end.append(b)
    length.append(c)
m=int(input())
for i in range(0,m):
    a,b=map(int,input().split(" "))
    if a==b:
        print(0)
    else:
        ind=start.index(a)
        temp=end[ind]
        result=[length[ind]]
        while temp!=b:
            ind=start.index(temp)
            temp=end[ind]
            result.append(length[ind])
        sum=0
        for item in result:
            sum=sum^item
        print(sum)