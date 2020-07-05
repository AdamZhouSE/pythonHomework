def arr44():
    n=int(input())
    for i in range(n):
        set=[]
        str=[x for x in input()]
        for x in str:
            if(x not in set):
                set.append(x)
        res=len(str)
        for d in range(0,len(str)):
            tmp = set.copy()
            for j in range(d,len(str)):
                if(str[j] in tmp):
                    tmp.remove(str[j])
                    if(len(tmp)==0):
                        res = min(res, j - d + 1)
                        break
        print(res)
    return

arr44()