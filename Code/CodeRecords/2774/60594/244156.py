def panduan(z)->bool:
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

n=(int)(input())
for index in range(0,n):
    A=input().split()
    now = []
    for index in range(len(A)):
        if panduan(A[index]):
            now.append((int)(A[index]))
    chengben=now[1]
    B=input().split()
    then=[]
    for index in range(len(B)):
        if panduan(B[index]):
            then.append((int)(B[index]))
    oc=sort(then)
    temp=0
    index=0
    while temp<=chengben:
        temp+=oc[index]
        index+=1
    print(index-1)