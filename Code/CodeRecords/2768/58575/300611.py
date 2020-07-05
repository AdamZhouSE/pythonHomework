n=int(input())
for i in range(n):
    str1=input().split(" ")
    str1=list(map(int,str1))
    
    A=str1[0]
    B=str1[1]
    M=str1[2]
    M_init=M
    
    res=0
    
    while M<A:
        M=M+M_init
    while M>=A and M<=B:
        M=M+M_init
        res=res+1
    print(res)