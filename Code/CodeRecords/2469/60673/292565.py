def test(str):
    num=len(set(str))
    b=set(list(str))
    res=[]
    temp=0
    copy=[]
    for i in b:
        copy.append(i)
    strr="".join(copy)
    for i in range(len(str)-num+1):
        j=i
        temp=0
        while(len(b)>0):
            if(j>=len(str)):
                break
            temp+=1
            if(str[j] in b):
                b.remove(str[j])
            j+=1
        if(temp!=0):
            res.append(temp)
        b=list(strr)
    return (min(res))

t=int(input())
for i in range(t):
    str=input()
    print (test(str))



