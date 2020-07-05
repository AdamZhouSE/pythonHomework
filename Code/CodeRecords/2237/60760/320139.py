def func(lists:list,n:int):
    arr=[i for i in range(1,n+1)]
    for i in lists:
        arr=arr[0:i[0]-1]+arr[i[0]-1:i[1]][::-1]+arr[i[1]:]
    return arr
if __name__ == '__main__':

    line=list(map(int,input().split(" ")))
    n=line[0]
    m=line[1]
    lists=[]
    for i in range(m):
        lists.append(list(map(int,input().split(" "))))
    res=func(lists,n)
    for i in res:
        print(i,end=" ")
    print()