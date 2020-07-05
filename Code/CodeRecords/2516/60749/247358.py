n=int(input())
res=[]
for x in range(0,n):
    res.append(input())
index_array=[]
def findindex(res):
    begin_array=[]
    end_array=[]
    for x in res:
        begin_array.append(x[0])
        end_array.append(x[1])
    res=[]

    for t in end_array:

        for k in range(0,len(begin_array)):
            if begin_array[k]>t:
                res.append(k)

                break

            res.append(-1)
    return res
print(findindex(res))