n=int(input())
for p in range(n):
    s=str(input())
    a=["ABCPQR","ADGJPRT","ABCPQ","ADGJP","ABCP","ADGJPR"]
    b=["RQP","JGDA","CBA","JGDA","CBA","JGDA"]
    for i in range(len(a)):
        if s==a[i]:
            s=b[i]
            break
    print(s)