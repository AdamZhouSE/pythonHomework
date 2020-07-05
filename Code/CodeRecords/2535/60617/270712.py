def divide():
    arr=list(eval(input()))
    arred=arr.copy()
    arred.sort()
    res=[]
    for i in range(0, len(arr)):
        idx = arred.index(arr[i])
        if not res:
            if i>=idx:
                start=idx
                end=i
                res.append([start, end])
            else:
                continue
        else:
            if i>=idx:
                start=idx
                end=i
                top=res[-1]
                if start<=top[1]:
                    top[1]=end
                    if start<top[0]:
                        top[0]=start
                else:
                    res.append([start, end])
            else:
                continue
    print(len(res))

if __name__=='__main__':
    divide()
