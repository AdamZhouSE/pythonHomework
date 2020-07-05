def tb2():
    n=int(input())
    for i in range(n):
        res=True
        str=[x for x in input()]
        str.sort()
        for i in range(len(str)-1):
            if(str[i+1]==str[i]):
                res=False
        print(1)if res else print(0)
    return 

tb2()