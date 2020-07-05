def func(arr:list):
    res=[]
    res.append(arr[0])
    del arr[0]

    for i in arr:
            if i>max(res):
                res.append(i)
            elif i<min(res):
                res=[i]+res
            else:
                for j in range(len(res) - 1):
                    if i >= res[j] and i < res[j + 1]:

                        if j == len(res) - 1:
                            res.append(i)
                        elif j == 0:
                            res = [i] + res
                        else:
                            res.insert(j + 1, i)
                        break

    return res

s=input()
lists=list(map(int,s[1:len(s)-1].split(',')))
print(func(lists))