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

A =input().replace("[",",").replace("]",",").replace(" ",",").split(",")
now = []
for index in range(len(A)):
    if panduan(A[index]):
        now.append((int)(A[index]))
m=[]
for i in now:
   m.append(i)
oc=sort(now)
i=0
j=len(oc)-1
while i<len(oc)-1:
    if oc[i]!=m[i]:
        break
    i+=1
while j>=0:
    if oc[j] != m[j]:
        break
    j -= 1
print(j-i+1)