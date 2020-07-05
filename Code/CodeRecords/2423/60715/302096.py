T=int(input())
while T>0:
    m,n=input().split()
    m=int(m)
    n=int(n)
    arr1=[int(n) for n in input().split()]
    arr2= [int(n) for n in input().split()]
    count=0
    for i in arr2:
        if i  in arr1:
            count+=1
    if count==len(arr2):
        print("Yes")
    else:
        print("No")
    T-=1