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

A=input().split(",")
now=[]
for i in A:
    now.append((int)(i))
now=sort(now)
print(now[(int)(len(now)/2)])

