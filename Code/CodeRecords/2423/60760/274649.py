def func(arr1:list,arr2:list):
    arr2=sorted(arr2)
    arr1=sorted(arr1)
    for i in range(len(arr1)-len(arr2)):
        if arr1[i:i+len(arr2)]==arr2:
            return "Yes"
    return "No"
tests=int(input())
list1s=[]
list2s=[]
for i in range(tests):
    l=input()
    list1s.append(list(map(int,input().split(" "))))
    list2s.append(list(map(int,input().split(" "))))
results=[]
for i in range(tests):
    print(func(list1s[i],list2s[i]))