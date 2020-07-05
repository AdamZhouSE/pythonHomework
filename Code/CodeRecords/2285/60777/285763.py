case=int(input())
for i in range(case):
    res=[]
    stock=int(input())
    price=[int(x) for x in input().split(' ')]
    start=-1
    end=-1
    for j in range(len(price)-1):
        if(price[j+1]>price[j]):
            if(j+1==len(price)-1):
                end=j+1
                res.append([start,end])
            if(end>=start):
                start=j
        else:
            if(end<start):
                end=j
                res.append([start,end])
            
    for j in range(len(res)):
        if(j!=len(res)-1):
            print('(',end='')
            print(res[j][0],res[j][1],end='')
            print(')',end=' ')
        else:
            print('(',end='')
            print(res[j][0],res[j][1],end='')
            print(')')
            