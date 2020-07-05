def operation(arr):
    allList=[]
    for i in range(len(arr)):
        string=""
        if i==len(arr)-1:
            allList.append(arr[i])
        for j in range(i,len(arr)):
            string+=arr[j]
            allList.append(string)
    stringSet=set(allList)
    return len(stringSet)

n=int(input())
myList=[]
inp=input().split()
for i in range(n):
    myList.append(inp[i])
    print(operation(myList))