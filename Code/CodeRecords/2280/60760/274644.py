def func(arr:list):
    for i in range(1,len(arr)+2):
        if arr.count(i)==0:
            return i

tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
for i in range(tests):
    print(func(lists[i]))