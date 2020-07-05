import math

def change(num,len_):
    str_=""
    while(num!=0):
        str_=str(num%2)+str_
        num//=2
    while(len(str_)!=len_):
        str_="0"+str_
    return str_

A=list(map(int,input().split(",")))
num=math.pow(2,len(A))
a=False
for i in range(1,int(num)):
    k=change(i,len(A))
    B=[]
    C=[]
    for j in range(len(k)):
        if k[j]=='1':
            B.append(A[j])
        else:
            C.append(A[j])
    if sum(B)*len(C)==sum(C)*len(B) and len(C)!=0 and len(B)!=0:
        a=True
        break
print(a)