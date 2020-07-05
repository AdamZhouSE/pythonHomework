
def sort5():
    a = input()
    set=[]
    str = list(a[2:len(a) - 2].split('],['))
    for i in range(len(str)):
        arr=[int(x) for x in str[i].split(',')]
        set.append(arr)
    r,c=len(set),len(set[0])
    for i in range(c):
        tmp=[]
        for h in range(max(r,c)):
            if(i+h>=c or h>=r):
                break
            tmp.append(set[h][h+i])
        tmp.sort()
        cnt=0
        for h in range(0,max(r,c)):
            if (i+h>= c or h >= r):
                break
            set[h][h+i]=tmp[cnt]
            cnt+=1
    for i in range(r):
        tmp=[]
        for h in range(max(r,c)):
            if(i+h>=r or h>=c):
                break
            tmp.append(set[h+i][h])
        tmp.sort()
        cnt=0
        for h in range(0,max(r,c)):
            if (h >= c or i+h >= r):
                break
            set[h+i][h]=tmp[cnt]
            cnt+=1
    print(set)
    return

sort5()