n=int(input())
result=[]
while n>0:
    ls=input().split(" ")
    ls=[int(x) for x in ls]
    A=ls[0]
    B=ls[1]
    C=ls[2]
    #要计算A^B%C
    while B>0:
        A=A*A
        B=B-1
    result.append(A%C)
    n=n-1
for i in range(0,len(result)):
    print(result[i])