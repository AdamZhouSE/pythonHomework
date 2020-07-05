t=int(input())
while t>0:
    t=t-1
    n,k=input().split(' ')
    n=int(n)
    k=int(k)
    s=[]
    for i in range(1,n+1):
        s.append(i)
    i=k-1
    length=n
    while length>1:
        temp=[]
        while i<length and length-len(temp)>1:
            temp.append(s[i])
            i=i+k
        i=i-length
        for item in temp:
            s.remove(item)
        length=len(s)
    print(s[0])