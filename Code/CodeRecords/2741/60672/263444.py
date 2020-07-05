def maxincreseorder(ar):
    ar=list(ar)
    i=1
    j=1
    for k in range(len(ar)-1):
        if int(ar[k+1])>int(ar[k]):
            j=j+1
        else:
            if j>i:
                i,j=j,i
            else:
                j=1
    if i>j:
        print(i)
    else:
        print(j)

er=input()
maxincreseorder(er)