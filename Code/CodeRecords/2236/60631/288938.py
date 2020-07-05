t=int(input())
data=[]
for ti in range(t):
    d=input().split(' ')
    #print(d)
    if d[0]=='1':
        data.append(int(d[1]))
        data=sorted(data)
    elif d[0]=='2':
        del data[data.index(int(d[1]))]
        data=sorted(data)
    elif d[0]=='3':
        print(data.index(int(d[1]))+1)
    elif d[0]=='4':
        print(data[int(d[1])-1])
    elif d[0]=='5':
        data.append(int(d[1]))
        data=sorted(data)
        print(data[data.index(int(d[1]))-1])
        del data[data.index(int(d[1]))]
    else:
        data.append(int(d[1]))
        data=sorted(data)
        print(data[data.index(int(d[1]))+1])
        del data[data.index(int(d[1]))]
    #print(data)