string=input()
i=0
result=[]
while i<len(string)-1:
    j=i
    k=i+1
    while k<len(string) and string[j]<=string[k]:
        if string[j]<string[k]:
            j=i
        else:
            j=j+1
        k=k+1
    while i<=j:
        i=i+k-j
        result.append(str(i))
if i<len(string):
    result.append(str(len(string)))
print(' '.join(result))