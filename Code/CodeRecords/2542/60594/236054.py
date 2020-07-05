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
oc = []
for index in range(len(A)):
    if (A[index].isdigit()):
        oc.append((int)(A[index]))
now=sort(oc)
max=1
qishi=0
qian=now[0]
for index in range(len(now)):
    if (now[index]-qian)>1:
        if index-qishi>max:
            max=index-qishi
        qishi=index
    qian=now[index]
print(max)