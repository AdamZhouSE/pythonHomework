def func(arr1:list,arr2:list):
    arr2=sorted(arr2)
    arr1=sorted(arr1)
    b00=1
    for i in arr2:
        if arr1.count(i)<arr2.count(i):
            b00=0
    if b00==1:
         return "Yes"
    else:
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