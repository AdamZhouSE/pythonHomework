def relativeSort():
    arr1=eval(input())
    arr2=eval(input())
    dic={}
    extra=[]
    result=[]
    for i in range(0,len(arr2)):
        dic[arr2[i]]=[i, 0]
    for num in arr1:
        if num not in dic:
            extra.append(num)
        else:
            dic[num][1]+=1
    for num in arr2:
        for i in range(0, dic[num][1]):
            result.append(num)
    extra.sort()
    result.extend(extra)
    print(result)
    
if __name__=='__main__':
    relativeSort()