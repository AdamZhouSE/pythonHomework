n=int(input())
result1=[]

for i in range(n):
    m=int(input())
    arr=input().split(" ")
    for p in range(m):
        arr[p] = "".join((lambda x: (x.sort(), x)[1])(list(arr[p])))
    arr1=list(set(arr))
    result=[0for q in range(len(arr1))]
    for k in range(len(arr1)):
        result[k]=arr.count(arr1[k])
    result.sort()
    result=' '.join(str(i) for i in result)
    result1.append(result)
for i in range(n):
    print(result1[i])