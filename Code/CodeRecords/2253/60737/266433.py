con = [int(n) for n in input().split( )]
l,m = con[0],con[1]
ret = [int(n) for n in input().split( )]
while m:
    cmd = [int(n) for n in input().split( )]
    op = cmd[0]
    if op==1:
        l,r,x = cmd[1],cmd[2],cmd[3]
        temp = ret[l-1:r]
        temp.sort()
        i = 0
        while temp[i]!=x:
            i += 1
        print(i+1)
    elif op==2:
        l,r,k = cmd[1],cmd[2],cmd[3]
        temp = ret[l-1:r]
        temp.sort()
        print(temp[k-1])
    elif op==3:
        pos,x = cmd[1],cmd[2]
        ret[pos-1] = x
    elif op==4:
        l,r,x = cmd[1],cmd[2],cmd[3]
        temp = ret[l-1:r]      
        temp.sort()
        i = 0
        while temp[i]<x and i<len(temp)-1:
            i += 1
        print(temp[i-1])
    else:
        l,r,x = cmd[1],cmd[2],cmd[3]
        temp = ret[l-1:r]
        temp.sort()
        i = len(temp)-1
        while temp[i]>x and i>=0:
            i -= 1
        print(temp[i+1])
    m -= 1
    