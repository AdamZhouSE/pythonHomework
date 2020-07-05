T=int(input())
for i in range(T):
    N=int(input())
    array1=input().split()
    array2=input().split()
    for j in range(N):
        array1[j]=int(array1[j])
        array2[j]=int(array2[j])
    array1.sort()
    array2.sort()
    result=[]
    for j in range(N):
        result.append(abs(array1[j]-array2[j]))
    print(max(result))