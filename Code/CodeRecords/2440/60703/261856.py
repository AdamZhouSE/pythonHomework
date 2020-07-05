List = eval(input())
res = []
if len(List)>=2:
    res.append(List[0])
    temp = List[1]
    if(List[0]>List[1]):
        res.insert(0,List[1])
    else:
        res.insert(1,List[1])

    for i in range(2,len(List)):
        for j in range(0,len(res)):
            temp = List[i]
            if(j==len(res)-1):
                res.append(temp)
                break
            if(j==0):
                if(res[0]>=temp):
                    res.insert(0,temp)
                    break
                elif (res[0] <= temp and res[0 + 1] >= temp):
                    res.insert(1, temp)
                    break
            else:
                if(res[j]<=temp and res[j+1]>=temp):
                    res.insert(j+1,temp)
                    break
    print(res)

else:
    print(res.sort())