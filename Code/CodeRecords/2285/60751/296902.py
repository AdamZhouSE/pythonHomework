num=int(input())
for i in range(num):
    N=int(input())
    nums=list(map(int,input().split(" ")))
    m=0
    n=0
    k=0
    sq=[]
    while(k<N-1):
        if nums[k]<nums[k+1]:
            n+=1
            if k==N-2:
                sq.append("("+str(m)+" "+str(n)+")")
        else:
            if m==n:
                m+=1
                n+=1
            else:
                sq.append("("+str(m)+" "+str(n)+")")
                m,n=k+1,k+1
        k+=1
    if len(sq)==0:
        print("没有利润")
    else:
        for j in range(len(sq)-1):
            print(sq[j],end=" ")
        print(sq[-1],end="")
        print()
