stra=input()
strb=input()
lena=len(stra)
lenb=len(strb)
count=0
for i in range(lena-lenb+1):
    isContain=True
    for j in range(lenb):
        if(stra[i+j]!=strb[j]):
            isContain=False
            break
    if(isContain):
        count+=1
        
print(count,end='')