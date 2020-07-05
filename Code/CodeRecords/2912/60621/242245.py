a=input().strip()
maxium=0
i,j=0,1
if i<len(a):
    tempSt=""+a[i]
    while j<len(a):

        if(tempSt.count(a[j])!=0):
            maxium = max(maxium, j - i)
            i=a.find(a[j],i)+1
            tempSt=a[i:j]

        else:
            tempSt+=a[j]
            j+=1
    if(j==len(a)):
        maxium=max(maxium,j-i)
print(maxium)