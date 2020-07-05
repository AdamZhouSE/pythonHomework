def func(arr:list,vegeis:int,maxprice:int ,maxdis:int):
    arr2=list(arr)
    for i in arr:
        if i[2]<vegeis or i[3]>maxprice or i[4]>maxdis:
            arr2.remove(i)
    temp=sorted(arr2, key=(lambda x:(x[1],x[0])))
    temp=temp[::-1]
    results=[]
    for i in temp:
        results.append(i[0])
    print(results)

lists=eval(input())
vegeis=int(input())
maxprice=int(input())
maxdis=int(input())
func(lists,vegeis,maxprice,maxdis)