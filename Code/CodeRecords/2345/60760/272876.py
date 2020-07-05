def func(arr:list):
    maxint=max(arr)
    miss=0
    for i in range(1,maxint+1):
        if arr.count(i)==0:
            miss=i
            break
    need=0
    for i in arr:
        if i!=miss:
            if arr.count(i)>=2:
                need=i
                break
    print(need,miss)

tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
res=[]
for i in lists:
    func(i)
