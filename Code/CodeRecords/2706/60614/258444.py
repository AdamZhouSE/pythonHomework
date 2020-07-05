str=eval(input())
i=0
while i<len(str):
    j=1
    while j<len(str[i]):
        k=i+1
        while k<len(str):
            if str[i][j] in str[k]:
                del(str[k][0])
                str[i]=str[i]+str.pop(k)
                k-=1
            k+=1
        j+=1
    i+=1
for i in str:
    j=0
    while j<len(i):
        key=i[j]
        while i.count(key)>1:
            i.remove(key)
            j-=1
        j+=1
print(str)