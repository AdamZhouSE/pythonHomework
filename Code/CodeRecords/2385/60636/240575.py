number=int(input())
lists=[]
for i in range(number):
    lists.append(int(input()))
for i in lists:
    length=i
    res=[]
    for i in range(pow(2,i)):
        result=str("{0:b}".format(i))
        while(len(result)<length):
            result="0"+result
        res.append(result)
    ans=res.copy()
    for i in range(len(res)):
        a=list(res[i])
        for z in range(length-1):
            if(int(a[z])==1&int(a[z+1])==1):
                ans.pop(ans.index(res[i]))
                break
    print(len(ans))