def func(arr:list):
    arr=sorted(arr)
    for i in range(int(len(arr)/2)):
        temp=arr[i*2]
        arr[i*2]=arr[i*2+1]
        arr[i*2+1]=temp
    for i in range(len(arr)-1):
        print(arr[i],end=" ")
    print(arr[len(arr)-1])
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))

for i in lists:
    func(i)