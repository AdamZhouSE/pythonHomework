def isAlter(s):
    index=True
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            index=False
    return index

T=int(input())
for m in range(T):
    n=int(input())
    result=""
    for i in range(1,n+1):
        if isAlter(bin(i).replace("0b","")):
            result=result+str(i)+" "
    result=result[:-1]
    print(result)