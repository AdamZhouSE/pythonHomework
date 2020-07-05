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
    if (A[index].isdigit()):
        now.append((int)(A[index]))



kuaishu=0
a=0
while a<len(now):
    jilu=len(now)
    b=a+1
    while b<len(now):
        if now[b]<now[a]:
            jilu=b
        b+=1
    if jilu==len(now):
        a=a+1
    if jilu<len(now):
        a=jilu+1
    kuaishu += 1
print(kuaishu)