str1=input()[1:-1].split(",")
res=[]
for i in str1:
    temp=list(map(int,i[1:-1].split(":")))
    trans1=temp[0]*60+temp[1]
    res.append(trans1)
res.sort()
res.reverse()
mintimeDirt=9999

i=0
while i<len(res)-1:
    j=i+1
    while j<len(res):
        Min=9999
        if 1440-res[i]-res[j]>=0:
            Min=min(res[i]-res[j],1440-res[i]-res[j])
        mintimeDirt=min(mintimeDirt,Min)
        j=j+1
    i+=1
print(mintimeDirt)