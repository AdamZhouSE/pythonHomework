def solve():
    n=int(input())
    list1=input().split(' ')
    list1=[int(list1[i]) for i in range(len(list1))]
    i=0
    a=0
    b=0
    c=0
    d=0
    m=0
    for i in range(n):
        if list1[i]==4:
            a=a+1
        elif list1[i]==3:
            b=b+1
        elif list1[i]==2:
            c=c+1
        elif list1[i]==1:
            d=d+1
        if c%2==0:
            if b>=d:
                m=a+b+int(c/2)
            else :
                if (d-b)%4==0:
                    m=a+int(c/2)+b+int((d-b)/4)
                else:
                    m=a+int(c/2)+b+int((d-b)/4+1)
        else:
            if b>=d:
                m = a + b + int(c / 2)+1
            else:
                if(d-b+2)%4==0:
                    m = a + int(c / 2) + b + int((d - b+2) / 4)
                else :
                    m=a+int(c/2)+b+int((d-b+2)/4+1)
    print(m)
    return
if __name__=='__main__':
    solve()