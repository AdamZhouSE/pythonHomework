def permutations(arr, position, end,k):
    if position == end:
        result.append(arr)
        if len(result)==k:
            for i in result[k-1]:
                print(i,end="")
            print("")
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end,k)
            arr[index], arr[position] = arr[position], arr[index]

n=int(input())
k=int(input())
arr = []
result=[]
for i in range(1,n+1):
    arr.append(i)
permutations(arr, 0, len(arr),k)