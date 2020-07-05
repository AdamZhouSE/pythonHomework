def tb19():
    n=int(input())
    for i in range(n):
        k=int(input())
        str=[x for x in input()]
        res=0
        for j in range(0,len(str)):
            if(str[j]!=' '):
                res+=int(str[j])
        if(res%3==0):
            print(1)
        else:print(0)
    return

tb19()