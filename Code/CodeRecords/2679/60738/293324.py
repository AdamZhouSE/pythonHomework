n=int(input())
def jiecheng(num):
    if(num==0):
        return 1
    else:
        res=1
        for j in range(1,num+1):
            res*=j
        return res
for i in range(n):
    N=int(input())
    if N==1:
        print(3)
    elif N==2:
        print(8)
    else:
        c2_1b=int(N*(N-1)*(N-2)/2)
        b_1=N
        c1_b1=N*(N-1)
        c_1=N
        c_2=int(N*(N-1)/2)
        a=1
        print(str(a+b_1+c_1+c_2+c1_b1+c2_1b))
        
        
        