def test():
    n=int(input())
    k=int(input())
    pwd=[]
    if(n==1):
        result=""
        for i in range(0,k):
            result=result+str(i)
        print(result)
        return
    result=""
    s=""
    for i in range(0,n):
        s=s+"0"
    s=s[1:len(s)]+str(k-1)
    result=s
    pwd.append(s)
    while(True):
        s1=s[1:len(s)]
        isEnd=True
        for j in range(k-1,-1,-1):
            s=s1+str(j)
            if(s in pwd):
                continue
            else:
                pwd.append(s)
                result=result+str(j)
                isEnd=False
                break
        if(isEnd):
            break
    print(result)
test()