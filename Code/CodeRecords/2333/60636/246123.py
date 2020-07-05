import math
x=int(input())
y=int(input())
bound=int(input())
res=[]
for i in range(2,bound+1):
    a=0
    while(a>=0):
        if(math.log(i-pow(x,a),y)!=int(math.log(i-pow(x,a),y))):
            a=a+1
        else:
            res.append(i)
            break
        if(i-pow(x,a)<0):
            break
print(res)
    