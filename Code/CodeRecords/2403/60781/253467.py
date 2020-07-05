can=int(input())
num=int(input())
list=[]
a=0
while a<num:
    list.append(0)
    a+=1
x=1
n=0
while can>0:
    if(can>x):
        list[n]+=x
        x+=1
        n+=1
    else:
        list[n]+=can
        x+=1
    can-=(x-1)
    if(n==num):
        n=0
print(list)