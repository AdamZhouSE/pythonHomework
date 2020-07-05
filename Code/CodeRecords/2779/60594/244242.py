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
    k=(int)(input())
    A =input().split(" ")
    now = []
    for index in range(len(A)):
        if panduan(A[index]):
            now.append((int)(A[index]))
    now=sort(now)
    a=now[0]
    b=now[k-1]
    temp=now[k-1]
    while True:
        if temp%a==0 and temp%b==0:
            print(temp)
            break
        else:
            temp+=1