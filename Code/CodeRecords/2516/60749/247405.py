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
    k=0

    for t in end_array:
        label=1
    

        for k in range(0,len(begin_array)):
            if begin_array[k]>t:
                result.append(k)
                label=0

                break
            

        if label==1:
            result.append(-1)
    return result
print(findindex(res))


