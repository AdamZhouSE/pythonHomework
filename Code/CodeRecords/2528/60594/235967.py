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
oc = []
for index in range(len(A)):
    if index>0 and index <(len(A)-1):
        oc.append((int)(A[index]))
print(sort(oc))