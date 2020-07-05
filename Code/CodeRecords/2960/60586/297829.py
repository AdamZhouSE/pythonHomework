def exam15():
    x=input().split(" ")
    m=int(x[0])
    n=int(x[1])
    a=input()
    b=input()
    record=[]
    for i in range(n):
        if b[i]==a[0] or b[i]=="*"or a[0]=="*":
            x=True
            for j in range(1,m):
                if b[i+1]==a[j]or b[i+1]=="*"or a[j]=="*":
                    i+=1
                else:
                    x=False
                    break
            if x:
                record.append(i-len(a)+2)
    print(len(record))
    for i in record:
        print(i,end=" ")
    print()
exam15()