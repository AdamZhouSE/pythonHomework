n=int(input())
result=[]
str=[]
i=n
g=0
while i>0:
    l=len(result)
    s=input()
    str=[]
    for j in s:
        str.append(j)
    for m in range(len(str)-len(set(str))+1):
        new_s=s[m:m+len(set(str))+g]
        a=[]
        for p in new_s:
            a.append(p)
        if len(a)==len(list(set(a))):
            result.append(len(set(str)))
        else :continue
    if len(result)==l:
        g=g+1
    else:
        g=0
        i=i-1
for k in range(n):
    print(result[k])