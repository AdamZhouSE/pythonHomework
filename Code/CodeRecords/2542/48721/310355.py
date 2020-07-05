s1=eval(input())
s1.sort()
length=len(s1)
if(length==0):print(0)
else:
    res=1
    index=1
    for i in range(length):
        if s1[i]-s1[i-1] == 1:
            index=index+1
        else:
            if s1[i]-s1[i-1] != 0:
                res=max(res,index)
                index=1
print(res)