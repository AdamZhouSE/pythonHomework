def isLucky(a):
    if(a==[0]):
        return 0
    res=[]
    for ele in a:
        if(ele<10):
            if(ele in res):
                return 0
            else:
                res.append(ele)
        else:
            num=ele%10
            while(int(ele/10)!=0):
                ele=int(ele/10)
                num=num*int(ele%10)
            if(num in res):
                return 0
            else:
                res.append(num)
    return 1
num=int(input())
li=[]
for i in range(num):
    li.append(input())
res=[]
for i in range(num):
    res.append([])
    for k in range(len(li[i])):
        for r in range(k+1,len(li[i])+1):
            arr=li[i][k:r]
            res[i].append(int(arr))
    print(isLucky(res[i]))