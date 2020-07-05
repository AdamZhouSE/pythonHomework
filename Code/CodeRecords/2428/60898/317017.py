T=eval(input())
for i in range(0,T):
    N=eval(input())
    arr=input().split()
    for j in range(0,N):
        arr[j]=int(arr[j])
    odd=[]
    even=[]
    for j in range(0,N):
        if arr[j]%2==0:
            even.append(arr[j])
        else:
            odd.append(arr[j])
    odd=sorted(odd)
    even=sorted(even)
    for j in range(0,len(odd)):
        print(odd[len(odd)-1-j],end=' ')
    for j in range(0,len(even)):
        if j!=len(even)-1:
            print(even[j],end=' ')
        else:
            print(even[j],end=' ')
            print('')