temp=[int(x) for x in input().split(',')]
li=[i for i in range(1,10)]
res=[]
some=li.copy()
def group(li,k,n):
    temp=[]
    if(k==1):
        if(n in li):
            li.remove(n)
            for i in some:
                if(not (i in li)):
                    temp.append(i)
            res.append(temp)
        return
    if(n<0):
        return
    if(len(li)<k):
        return
    get=li[0]
    if(get>n):
        return
    pre=li.copy()
    pre.remove(get)
    sec=pre.copy()
    group(pre,k-1,n-get)
    some.remove(get)
    group(sec,k,n)
    some.append(get)
    some.sort()
group(li,temp[0],temp[1])    
print(res)