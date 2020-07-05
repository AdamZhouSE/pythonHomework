n=input()
b=n
res=[]
number=[]
for i in range(len(n)-1,-1,-1):
    if(len(res)==0):
        res.append(b[i:len(n)])
        number.append(i)
    else:
        if(b[i:len(n)]<res[0]):
                res.insert(0,b[i:len(n)])
                number.insert(0,i)
        if(b[i:len(n)]>res[len(res)-1]):
                res.insert(len(res), b[i:len(n)])
                number.insert(len(res), i)
        else:
            for j in range(0,len(res)-1):
                if(b[i:len(n)]>res[j] and b[i:len(n)]<res[j+1]):
                    res.insert(j+1,b[i:len(n)])
                    number.insert(j+1,i)
res.sort()
re=[]
for i in range(len(res)):
    if(i!=(len(res))):
        print(len(res)-len(res[i])+1,end=' ')