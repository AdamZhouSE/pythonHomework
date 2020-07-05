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
ar1=input().split(",")
arr1=[]
for index in range(len(ar1)):
    if panduan(ar1[index]):
        arr1.append((int)(ar1[index]))
n=(int)(input())
arr1=sort(arr1)
print(arr1[len(arr1)-n])