n=int(input())
for I in range(n):
    s=list(input())
    print(s)
    res=0
    tmp=0
    xxx=[]
    if len(s)%2==0:
        res=-1
    else:
        for i in s:
            if i=='{':
                tmp+=1
                
            else:
                if tmp==0:
                    xxx.append(i)
                else:
                    tmp-=1
                print(tmp)
    print(res)