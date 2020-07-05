t=int(input())
while t>0:
    t=t-1
    s=input()
    k=int(input())
    max=0
    for i in range(0,len(s)-k+1):
        temp=''
        for j in range(i,len(s)):
            temp=temp+s[j]
            se=set(temp)
            length=len(se)
            if length<=k:
                if len(temp)>max:
                    max=len(temp)
            else:
                break
    print(max)
        