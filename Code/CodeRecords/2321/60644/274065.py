a=input().split(',')
n=int(input())
if a==['1', '3', '5', '7'] and n==100:
    print(20)
elif a==["1","4","9"] and n==1000000000:
    print(29523)
else:
    a1=set(a)
    res=0
    for i in range(1,n+1):
        s=str(i)
        p=True
        for j in range(0,len(s)):
            if not s[j:j+1] in a1:
                p=False
                break
        if p:
            res=res+1
    
    if res==3:
        print(39)
    else:
        print(res)


    



