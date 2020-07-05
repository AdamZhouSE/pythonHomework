numlist=list(input(""))
maxsum=max(numlist)
for i in range(len(numlist)-1):
    for j in range(i+1,len(numlist)+1):
        maxsum=max(maxsum,sum(numlist[i:j]))
print(maxsum)