n=int(input())
result = [0for i in range(n)]
for i in range(n):
    sum=input().split(" ")
    arr1=input().split(" ")
    arr2=input().split(" ")
    c=list(set(arr1).union(set(arr2)))
    result[i]=len(c)
for p in range(n):
    print(result[p])

   