T=int(input())
for i in range(0,T):
    s=list(input())
    count=0
    temp=""
    yuan=['a','e','i','o','u']
    s.sort()
    for i in s:
        if i in yuan:
            continue
        if i!=temp:
            count+=1
            temp=i
    if(count%2==0):       
        print("SHE!")
    else:print("HE!")