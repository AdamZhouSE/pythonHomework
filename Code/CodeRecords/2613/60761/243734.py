def Connellseq(n):
    i=0 #已打印的数量
    j=1 #每次打的数量
    m=1 #每次打的第一个数
    while(True):
        if(i<n):
            if(i+j>n):
                j=n-i
            for k in range(j):
                a=m+2*k
                if(i==n-j and k==j-1):
                    print(a)
                    break 
                else:
                    print(a,end=" ")
            m=a+1
            i=i+j
            j=j+1
        else:
            break

n=int(input(""))
for i in range(n):
    Connellseq(int(input("")))