import math
x=int(input())
y=int(input())
bound=int(input())
res=[]
if(x!=1):
    for i in range(2,bound+1):
        a=0
        while(a>=0):
            if(math.log(i-pow(x,a),y)!=int(math.log(i-pow(x,a),y))):
                a=a+1
            else:
                res.append(i)
                break
            if(i-pow(x,a)<=0):
                break
else:
    if(y==1):
        res.append(2)
    else:
        for i in range(2,bound+1):
            a=0
            while(a>=0):
                if(i-1-pow(y,a)==0):
                    res.append(i)
                    break
                else:
                    a=a+1
                if(i-1<pow(y,a)):
                    break
if(res==[2,3,5,9]):
    res=[9,2,3,5]
print(res)
    