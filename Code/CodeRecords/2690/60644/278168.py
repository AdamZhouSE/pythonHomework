def f(start,char,index,str,res,l,s):

    if index==l-1:
        for i in range(start,len(str)):
            if str[i:i+1]==char:
                res+=1

    else:
        for i in range(start,len(str)):
            if str[i:i+1]==char:
                res=f(i+1,s[index+1],index+1,str,res,l,s)
    return res



t=int(input())
for i in range(0,t):
    x=input().split()
    l1=int(x[0])
    l2=int(x[1])
    p=input().split()
    str=p[0]
    s=p[1]
    res=0
    print(f(0,s[0:1],0,str,res,len(s),s))
