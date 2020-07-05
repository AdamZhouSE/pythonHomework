def panduan(z:int)->bool:
    try:
        z = int(z)
        return isinstance(z, int)
    except ValueError:
        return False
def sort(A:list)->list:
    oc=[]
    a=1
    b=len(A)
    while a<=b:
        min=0
        for index in range(len(A)):
            if A[index]<A[min]:
                min=index
        oc.append(A[min])
        del(A[min])
        a+=1
    return oc

A =input().replace("[",",").replace("]",",").split(",")
now = []
for index in range(len(A)):
    if panduan(A[index]):
        now.append((int)(A[index]))
oc=sort(now)
a=0
x=True
while x==True:
    a+=1
    for index in range(len(oc)):
        if oc[index]==a:
            break
        if index==len(oc)-1:
            x=False

print(a)
