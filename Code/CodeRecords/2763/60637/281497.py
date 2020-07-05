tests=(int)(input())
for i in range(tests):
    m,n=map(int,input().split(' '))
    order=[]
    def get_order(temp,i):
        global n,m,order
        if(temp[-1]<=m):
            if (len(temp) == n):
                order.append(temp)
            else:
                for j in range(i*2,m+1):
                    temp.append(j)
                    get_order(list.copy(temp),j)
                    temp=temp[:-1]
    for i in range(1,(int)(m/pow(2,n-1))+1):
        get_order([i],i)
    print(len(order))
