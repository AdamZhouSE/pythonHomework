n=int(input())
for i in range(0,n):
    str=input()
    set1=set()
    for i in str:
        set1.add(i)
    k=len(set1)
    res=100000000000
    for j in range(0,len(str)-k+1):
        for t in range(j+k,len(str)+1):
            flag=True
            for m in set1:
                if m not in str[j:t]:
                    flag=False
                    break
            if flag:
                res=min(res,t-j)
                break
    print(res)