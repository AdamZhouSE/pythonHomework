def test16():
    t=int(input())
    x=input().split(" ")
    num=[]
    c=[]
    for item in x:
        num.append(int(item))
    for i in range(1,len(num)):
        if num[i-1]>=num[i]:
            c.append(num[i-1])
    c.append(num[len(num)-1])
    result=str(c[0])
    for i in range(1,len(c)):
        result=result+" "+str(c[i])
    return str(len(c))+"\n"+result
print(test16())