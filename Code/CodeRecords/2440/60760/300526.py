def func(arr:list):
    res=[0]
    res.append(arr[0])
    del arr[0]
    for i in arr:
        for j in range(len(res)-1):
            if i>=res[j] and i<res[j+1]:
                indexs=res.index(j)
                res.insert(indexs+1,i)
                break
    res.remove(0)
    return res

s=input()
lists=list(map(int,s[1:len(s)-1].split(',')))
print(func(lists))