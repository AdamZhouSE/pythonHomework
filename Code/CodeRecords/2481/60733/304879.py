t=int(input())
for i in range(t):
    n,m=input().split()
    n,m=int(n),int(m)
    arr1=[int(i) for i in input().split()]
    arr2=[int(i) for i in input().split()]
    count=0
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            count+=1
            for j in range(arr2.count(arr1[i])):
                arr2.remove(arr1[i])
    print(count)     