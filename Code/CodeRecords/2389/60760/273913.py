def func(arr:list):
    arr=sorted(arr)
    for i in range(int(len(arr)/2)):
        temp=arr[i*2]
        arr[i*2]=arr[i*2+1]
        arr[i*2+1]=temp
    for i in arr:
        print(i,end=" ")
    print()
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))

for i in lists:
    func(i)