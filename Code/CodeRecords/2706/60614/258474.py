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
    j=1
    while j<len(i):
        key=i[j]
        k=len(i)-1
        while k>j:
            if i[k]==key:
                del(i[k])
            k-=1
        j+=1
print(str)