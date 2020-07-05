T=int(input())
for sample in range(T):
    n=int(input())
    tmp=n
    ans=''
    while tmp>9:
        tmp-=9
        ans='9'+ans
    ans=str(tmp)+ans
    ans+='0'*n
    print(ans)