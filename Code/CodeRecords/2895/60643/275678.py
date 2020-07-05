if __name__=="__main__":
    lst=eval(input())
    m=lst[0]
    n=lst[1]
    res=m
    for i in range(m,n+1):
        res&=i
    print(res)