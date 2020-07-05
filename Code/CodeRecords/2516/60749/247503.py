n=int(input())
res=[ ]
for x in range(0,n):
    res.append(input())

def findindex(res):
    begin_array=[]
    end_array=[]
    for x in res:
        begin_array.append(x[0])
        end_array.append(x[1])
    result=[]


    for t in end_array:
        temp=[]
        for k in range(0,len(begin_array)):

            if begin_array[k]>=t:
                temp.append(begin_array[k])

        if len(temp)==0:
            result.append(-1)
        else:
            minvalue=min(x for x in temp)
            result.append(begin_array.index(minvalue))
    return result
print(findindex(res))


