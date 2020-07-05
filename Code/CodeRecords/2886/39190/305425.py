def func18(arr):
    res=[]
    count=0
    for i in arr:
        try:
            res.index(i)
            res.remove(i)
        except:
            res.append(i)
            count=max(count,len(res))
    print(count)

nums=int(input())
arr=input().split(" ")
func18(arr)