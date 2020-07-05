res=[]
n=int(input())
for i in range(n):
    res.clear()
    number=list(input())
    judge=True
    i=0
    while i<len(number) or judge==False:
        result=int(number[i])
        if result in res:
            judge=False
            break
        else:
            res.append(result)
        j=i+1
        while j<len(number):
            result=int(number[j])*result
            if result in res:
                judge = False
                break
            else:
                res.append(result)
            j=j+1
        i=i+1
    if judge==True:
        print(1)
    else:
        print(0)