a=int(input())
b=int(input())
num=a*b
li=[]
for i in range(0,num):
    li.append(0)
n=int(input())
min1=0
min2=0
for i in range(n):
    o=list(eval(input()))
    if(i==0):
        min1=int(o[0])
        min2=int(o[1])
    else:
        if(int(o[0])<min1):
            min1=int(o[0])
        if(int(o[1])<min2):
            min2=int(o[1])
print(min(min1*min2,a*min2,b*min1))