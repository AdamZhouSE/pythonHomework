n=int(input())
str=""
result=[]
for i in range(n):
    s=input()
    p=s
    j=len(s)
    while j>0:
        if s[j-1]>='1' and s[j-1]<='9':
            q=p
            for i in range(int(s[j-1])-1):
                for k in range(j,len(q)):
                    p=p+q[k]
        j=j-1
    for i in p:
        if i!="[" and i!="]"and (i>'9'or i<'0'):
            str=str+i
    result.append(str)
    str=""
for i in range(len(result)):
    print(result[i])