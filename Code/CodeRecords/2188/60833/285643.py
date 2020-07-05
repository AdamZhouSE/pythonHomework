num_list=input().split(" ")
k=int(num_list[1])
stra=str(input())
strb=str(input())
n=int(input())
result=[]
for i in range(0,n):
    num_list = input().split(" ")
    s=int(num_list[0])
    t=int(num_list[1])
    l=int(num_list[2])
    r=int(num_list[3])
    res=0
    j=s-1
    subp=strb[l-1:r]
    while(j<=t-len(subp)):
        if stra[j:j+len(subp)]==subp:
            res+=k-(j+1)
            j+=len(subp)
        else:
            j+=1
    result.append(res)
for j in result:
    print(j)