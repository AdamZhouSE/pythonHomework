def func(list0:list,k:int):
    n=int(len(list0)/k)
    diside=[]
    for i in range(n):
        temp=list0[i*k:(i+1)*k]
        diside.append(temp)
    diside.append(list0[n*k:len(list0)])
    result=[]
    for i in diside:
        result=result+i[::-1]
    return result

tests=int(input())
res=[]
for i in range(tests):
    k=list(map(int,input().split(" ")))[1]
    list0=list(map(int,input().split(" ")))
    res.append(func(list0,k))
for i in res:
    for j in range(len(i)-1):
        print(i[j],end=" ")
    print(i[len(i)-1])