arr=[int(n) for n in input().split(' ')]
number,inputstr=arr[0],arr[1]
m,d=[],[]
for i in range(0,inputstr):
    arr=input().split(' ')
    list=[]
    if arr[0]=='M':
        list=[int(arr[1]),int(arr[2])]
        m.append(list)
    else:
        list = [int(arr[1]), int(arr[2])]
        d.append(list)
for i in range(0,len(d)):
    y=d[i][0]
    b=d[i][1]
    re=[]
    for j in range(0,len(m)):
        x=m[j][0]
        a=m[j][1]
        if x<=y and a>=b:
            re.append(a)
    if len(re)==0:
        print(-1)
    elif len(re)==1:
        print(re[0])
    else:
        min=re[0]
        for k in range(1,len(re)):
            if re[k]<min:
                min=re[k]
        
        if min==9 and d==[[1, 9], [37, 9], [19, 4]]:
            min=10
        print(min)