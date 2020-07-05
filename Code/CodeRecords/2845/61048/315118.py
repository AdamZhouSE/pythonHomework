def arr22():
    n=int(input())
    set=[]
    for i in range(n):
        set.append([int(x) for x in input().split(' ')])
    set.sort(key=lambda x:x[0])
    tmp=set.copy()
    tmp.sort(key=lambda x:x[1])
    if(tmp==set):
        print("Poor Alex")
    else:
        print("Happy Alex")
    return

arr22()