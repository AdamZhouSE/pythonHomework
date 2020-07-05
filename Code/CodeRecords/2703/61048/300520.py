def search3():
    set=[]
    str = list(input()[2: - 2].split('], ['))
    for i in range(len(str)):
        arr=[int(x) for x in str[i].split(',')]
        set.append(arr)
    circles=[int(x) for x in range(len(set))]
    res=len(set)
    for i in range(len(set)):
        for j in range(len(set)):
            if(i!=j and set[i][j]==1):
                x1=find(i,circles)
                x2=find(j,circles)
                if(x1!=x2):
                    circles[x1]=x2
                    res-=1
    print (res)
    return

def find(no,circles):
    return no if circles[no]==no else find(circles[no],circles)

search3()